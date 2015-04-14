Predicting-Hot-Technology-Trends
================================

# Install
*Must have Vagrant and Ansible set up on the machine to create the VM.* 
[Vagrant Install](https://docs.vagrantup.com/v2/installation/)
[Ansible Install](http://docs.ansible.com/intro_installation.html)

1. Clone the repo
2. Run `vagrant up` to create the VM
3. `vagrant ssh` will ssh you into the VM

# Usage

```shell
python /vagrant/generateReport.py
```

This will generate the report that we demoed for the expo. It could take a few minutes to run, as it also is creating all the images that may be required for the report. The generated report and images are put in the `/vagrant/generated_report` folder.

# Serving Reports

Currently nginx is set up to serve the `/vagrant/generated_report` directory, on port 80. With Vagrant, we have also forwarded port 4567 on the host machine to port 80 on the VM. So once you generate a report you should be able to go to `http://localhost:4567/expo.html` on the host machine and view the report.
