import subprocess
from subprocess import Popen, PIPE
from subprocess import check_output
from flask import Flask


def get_pod_ip():
    stdout = check_output(['./test.sh']).decode('utf-8')
    return stdout
	
app = Flask(__name__)

@app.route('/myPodInfo',methods=['GET',])
def home():
    return "+get_pod_ip()+"

app.run(debug=True)

return get_pod_ip()