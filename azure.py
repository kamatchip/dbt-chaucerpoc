#Azure Function Code (Python) to Run PowerShell Script
 
import subprocess
import logging
import os
 
def main():
    try:
        # Define the PowerShell script path
        #script_path ="C:\\home\\site\\wwwroot\\run_dbt.ps1"  # Adjust based on your deployment location
        # script_path = r".\scripts\dbt_run.ps1" 

        # print(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path])
        # Run the PowerShell script
        result = subprocess.run(["dbt" , "run"],
                                capture_output=True, text=True)


# powershell.exe -ExecutionPolicy Bypass -File C:\Users\PocChausar2\POC_CH\scripts\dbt_run.ps
        # Log output
        print(f"DBT Output: {result.stdout}")
        print(f"DBT Error: {result.stderr}")

        return
        {
            "statusCode": 200 if result.returncode == 0 else 500,
            "body": result.stdout if result.returncode == 0 else result.stderr
        }
    
    except Exception as e:
        logging.error(f"Error running dbt script: {str(e)}")
        return {"statusCode": 500, "body": str(e)}
    

main()
