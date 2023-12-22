import psycopg2
import subprocess
import os
from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify
from flask_cors import CORS,cross_origin
#to run the app flask run --debug

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# subprocess.run(["python", "../db/initDB.py"])

PORT = int(os.environ.get('PORT'))

DB_HOST = os.environ.get('DB_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
POSTGRES_DB  = os.environ.get('POSTGRES_DB')

def db_conn():
    #TODO:CHANGE THIS TO DB FOR THE CONTAINER TO WORK
    conn = psycopg2.connect(database = POSTGRES_DB, host = DB_HOST, user = POSTGRES_USER, 
                                            password = POSTGRES_PASSWORD, port = POSTGRES_PORT)
    return conn

@app.route('/getDoctors')
@cross_origin()
def get():
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('''SELECT id,name FROM Users WHERE role = 'doctor' ''')
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

@app.route('/addAppointment', methods=['PATCH'])
def addAppointment():
    doctor_id = request.json['doctorID']
    Date = request.json['Date']
    Hour = request.json['Hour']
    print(Date,doctor_id,Hour)
    if doctor_id is None:
        return jsonify('please enter valid doctor id!'),404
    if Date is None:
        return jsonify('please enter valid Date!'),404
    if Hour is None:
        return jsonify('please enter valid Hour!'),404
    
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT id FROM Users WHERE id={doctor_id} AND role = 'doctor' ''')
    checkID = cur.fetchall()
    if not checkID:
        return jsonify('there is no doctor with that id!'),404
    
    cur.execute(f'''SELECT * FROM Appointments WHERE Date = '{Date}' AND Hour = '{Hour}' AND createdBy = {doctor_id}''')
    checkSlot = cur.fetchall()
    if checkSlot:
        return jsonify('this doctor already has this slot!'),409
    
    cur.execute(f'''INSERT INTO Appointments (createdBy,Date,Hour) VALUES ({doctor_id},'{Date}','{Hour}')''')
    
    cur.close()
    conn.commit()
    conn.close()
    return jsonify('appointment added successfully!'),201


@app.route('/getDoctorAppointments', methods=["POST"])
def getDoctorAppointments():
    DiD = request.json["doctorID"]
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f'''SELECT name FROM Users WHERE id={DiD} AND role = 'doctor' ''')
    checkName = cur.fetchall()
    if not checkName:
        return jsonify("this doctor does not exist"),404
    cur.execute(f'''SELECT Date, Hour FROM Appointments WHERE createdBy = {DiD}''')

    #parsing date and time into json
    # checkAppointmentDate = [
    # {'id':appointment[0],'Date': appointment[1].strftime('%Y-%m-%d'), 'Hour': appointment[2].strftime('%H:%M:%S')}
    # for appointment in cur.fetchall()
    # ]
    checkAppointmentDate = cur.fetchall()
    
    if not checkAppointmentDate:
        return jsonify("this doctor does not have any appointments yet!"),404
    
    cur.close()
    conn.commit()
    conn.close()
    #json.dumps(checkAppointmentHour,default=str)
    return jsonify(checkAppointmentDate),200

@app.route('/getDoctorAppointmentsWithId', methods=["POST"])
def getDoctorAppointmentsWithId():
    DiD = request.json["doctorID"]
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(f'''SELECT name FROM Users WHERE id={DiD} AND role = 'doctor' ''')
    checkName = cur.fetchall()
    if not checkName:
        return jsonify("this doctor does not exist"),404
    cur.execute(f'''SELECT id, Date, Hour FROM Appointments WHERE createdBy = {DiD} AND occupiedBy IS NULL''')

    #parsing date and time into json
    # checkAppointmentDate = [
    # {'id':appointment[0],'Date': appointment[1].strftime('%Y-%m-%d'), 'Hour': appointment[2].strftime('%H:%M:%S')}
    # for appointment in cur.fetchall()
    # ]
    checkAppointmentDate = cur.fetchall()
    
    if not checkAppointmentDate:
        return jsonify("this doctor does not have any appointments yet!"),404
    
    cur.close()
    conn.commit()
    conn.close()
    #json.dumps(checkAppointmentHour,default=str)
    return jsonify(checkAppointmentDate),200


@app.route('/reserveSlot', methods=['PATCH'],)
def reserveSlot():
    SiD = request.json["slotID"]
    patientID = request.json['patientID']
    
    if patientID is None:
        return jsonify('please enter valid doctor id!'),404
    
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT * FROM Appointments WHERE occupiedBy = {patientID} AND id={SiD} ''')
    checkIfIAlreadyReserved = cur.fetchall()
    if checkIfIAlreadyReserved:
        return jsonify("you already reserved this slot!"),409
    
    cur.execute(f'''SELECT * FROM Appointments WHERE occupiedBy IS NULL AND id={SiD} ''')
    checkSlotFree = cur.fetchall()
    if not checkSlotFree:
        return jsonify("this slot is already occupied with another patient!"),409
    
    cur.execute(f'''UPDATE Appointments SET occupiedBy={patientID} WHERE id={SiD}''')
    
    cur.close()
    conn.commit()
    conn.close()
    
    return jsonify("reserved successfully"),200
    

@app.route('/getReservations',methods=['POST'])
def getReservations():
    PiD = request.json['patientID']
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT id,Date,Hour FROM Appointments WHERE occupiedBy = {PiD}''')
    
    # reservations = [
    # {'id':appointment[0],'Date': appointment[1].strftime('%Y-%m-%d'), 'Hour': appointment[2].strftime('%H:%M:%S')}
    # for appointment in cur.fetchall()
    # ]
    
    reservations = cur.fetchall()
    
    if not reservations:
        return jsonify('you have no reservations!'),404
    
    cur.close()
    conn.close()
    return jsonify(reservations),200

@app.route('/updateReservation',methods=['POST'])
def updateReservation():
    PiD = request.json['patientID']
    slotID = request.json['slotID']
    newSlotID = request.json['newSlotID']
    
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT * FROM Appointments WHERE occupiedBy = {PiD} AND id={slotID} ''')
    checkIfReserved = cur.fetchall()
    if not checkIfReserved:
        return jsonify("you dont have this appointment reserved to be able to change it"),404
    
    #removes the patient from old appointment completely
    cur.execute(f'''UPDATE Appointments SET occupiedBy = NULL WHERE id={slotID} ''')
    
    cur.execute(f'''SELECT * FROM Appointments WHERE id = '{newSlotID}' AND occupiedBy IS NULL ''')
    checkIfSlotExists = cur.fetchall()
    if not checkIfSlotExists:
        return jsonify('this slot you are trying to change to does not exist!'),404
    
    
    cur.execute(f'''UPDATE Appointments SET occupiedBy={PiD} WHERE id={newSlotID} ''')
    cur.close()
    conn.commit()
    conn.close()
    return jsonify("Updated successfully!"),200

@app.route('/cancelReservation',methods=['POST'])
def cancelReservation():
    PiD = request.json['PatientID']
    slotID = request.json['slotID']
    
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT * FROM Appointments WHERE occupiedBy = {PiD} AND id={slotID} ''')
    checkIfReserved = cur.fetchall()
    if not checkIfReserved:
        return jsonify("you dont have this appointment reserved to be able to cancel it"),404
    
    cur.execute(f'''UPDATE Appointments SET occupiedBy = NULL WHERE id={slotID} ''')
    
    cur.close()
    conn.commit()
    conn.close()
    return jsonify('Cancelled successfully!'),200

# @app.route("/test",methods = ['POST'])
# def test():
#     data=request.get_json()
#     return jsonify(data),200

@app.route('/signUp', methods=['POST'])
def signUp():
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']
    role = request.json['role']
    
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT name FROM Users WHERE email = '{email}' ''')
    checkIfUserAlreadyExists = cur.fetchall()
    
    if checkIfUserAlreadyExists:
        return jsonify("this user already exists!"),409
    
    cur.execute(f'''INSERT INTO Users (name,email,password,role) VALUES ('{name}','{email}','{password}','{role}') ''')
    
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify("user added successfully"),201


@app.route('/signIn',methods=['POST'])
def signIn():
    email = request.json['email']
    password = request.json['password']
    
    conn = db_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute(f'''SELECT name,id,role FROM Users WHERE email = '{email}' AND password = '{password}' ''')
    checkIfAccountCorrect = cur.fetchone()
    
    if not checkIfAccountCorrect:
        return jsonify("invalid account credentials"),404
    
    cur.close()
    conn.close()
    return jsonify(checkIfAccountCorrect),200

@app.route('/')
def home():
    return '<h1><center>home</center></h1>'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT", 5000)), debug=True)
