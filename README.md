# Servo Data Visualization

## Rest Endpoint
The rest endpoint available to ingest data can be reached at the HTTPS endpoint
https://api.nebullam.com/challengeData

## Grabbing the Data via the Shell

### Curl
Prior to visualizing the data, let's quickly inspect what we're working with.
Prior to utilizing a programming language, we can first curl the endpoint
on the shell to view the JSON data returned

```sh
curl -X GET https://api.nebullam.com/challengeData
``` 

### Curl w/ pipe
To take this a step further for readability sake , let's pipe our response
to the json.tool python module.

```sh
curl -X GET https://api.nebullam.com/challengeData | python -m json.tool
```

## The Data
From the data below, it looks like we have data on three Servo Motors.
The data includes an:
  - servoID - an integer that defines what motor the data belongs to
  - position - the position of the motor, what are the units? 
  - isCalibrated - whether or not the motor is calibarted.

### Sample Data
```json
{
    "data": [
        {
            "isCalibrated": true,
            "position": 100,
            "servoID": 1
        },
        {
            "isCalibrated": true,
            "position": 23,
            "servoID": 2
        },
        {
            "isCalibrated": true,
            "position": 56,
            "servoID": 3
        }
    ]
}
```

# A simple Flask App
In order to display the Servo Motor data in an interesting way, quickly, let's 
utilize flask to serve a simple html file with some simple CSS

## Setup

- Clone the repository
```shell
git clone git@github.com:NickHerrig/motor-dashboard.git
```

- Build the application
```shell
Make build
```

- Run the application
```shell
Make run 
```

- Navigate to the dashboard at http://localhost:5000 

- Clean up 
```shell
Make clean 
```
