from flask import Flask,request,jsonify
import subprocess


app=Flask(_name_)

@app.route('/trigger_dbt',methods=['POST'])

def trigger_dbt()
   try:
    #Run the dbt command
    result=subprocess.run(['dbt','run']),capture_output=True, text=True

    #Return the output of the dbt command
    return jsonify({
        'status':'success',
        'output': result.stdout,
        'error':result.stderr
    }),200

    except Exception as e:
        return jsonify({
            'status':'error'
            'message':str(e)
        }),500

 if _name_=='main'
  app.run(host='0.0.0.0',port=5000)