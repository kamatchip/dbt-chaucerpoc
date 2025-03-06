$DBT_Project_Path = "C\Users\PocChausar2\POC_CH\"

cd $DBT_Project_Path

dbt run --select .\models

if ($?){
    Write-Output "dbt execution completed successfully"
    exit 0
}else {
    Write-Output "dbt execution failed"
    exit 1
}
