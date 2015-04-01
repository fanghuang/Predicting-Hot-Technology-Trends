Predicting-Hot-Technology-Trends
================================

# Install
*Must have Vagrant and Ansible set up on the machine to create the VM.* 

1. Clone the repo
2. Run 'vagrant up' to create the VM
3. 'vagrant ssh' will ssh you into the VM

# Usage

'''shell
python /vagrant/generateReport.py
'''
This will generate the report that we demoed for the expo. It will take a second to run, as it also is creating all the images that may be required for the report. The generated report and images are put in the /vagrant/generated_report folder.
