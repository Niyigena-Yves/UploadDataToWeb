import serial
import requests
# ser = serial.Serial(port='COM6',
#                     baudrate=9600,
#                     parity=serial.PARITY_NONE,
#                     stopbits=serial.STOPBITS_ONE,
#                     bytesize=serial.EIGHTBITS,
#                     timeout=1)
# ser.flush()
 

def upload_data(filedata):
    with open(filedata, "rb") as a_file:
        data = {"transaction": a_file}

        try:
            res = requests.post('http://localhost:5500/uploads/transaction', files=data)
            res.raise_for_status()
            if res is not None:
                return res.json()
        except requests.exceptions.HTTPError as err:
            print(f"Error {res.status_code}: {res.json()}, for {res.request}: {res.url}")
        except Exception as err:
            print(f"Error {err}")


if __name__ == '__main__':

 # call upload function

 response = upload_data("transactions.txt")
 if(response['message']):
     print(response['message'])
    #  ser.write(response['message'])