import csv
import os

file_path = os.getcwd()
headers = ["Timestamp", "Application Name", "Description", "Status", "Code", ""]


class Failed:
    failed_dict = {}

    def __init__(self, timestamp='01-01-2000', application_name='app_name',
                 description='description', status='Failed', code='code'):
        self.timestamp = timestamp
        self.application_name = application_name
        self.description = description
        self.code = code
        self.status = status

    def read_log_file(self):
        with open(file_path + '\\log.csv', 'r') as log:
            for i in log:
                if 'Failed' in i:
                    print(i)

    def set_log_data(self, timestamp='01-01-2000', application_name='app_name',
                     description='description', status='Failed', code='code'):
        failed_values = []
        self.failed_dict[headers[0]] = timestamp
        self.failed_dict[headers[1]] = application_name
        self.failed_dict[headers[2]] = description
        self.failed_dict[headers[3]] = status
        self.failed_dict[headers[4]] = code
        failed_values.append(self.failed_dict)
        return failed_values


class Success:
    success_dict = {}

    def __init__(self, timestamp='01-01-2000', application_name='app_name',
                 description='description', status='Success'):
        self.timestamp = timestamp
        self.application_name = application_name
        self.description = description
        self.status = status

    def read_log_file(self):
        with open(file_path + '\\log.csv', 'r') as log:
            for i in log:
                if 'Success' in i:
                    print(i)

    def set_log_data(self, timestamp='01-01-2000', application_name='app_name',
                     description='description', status='Success'):
        success_values = []
        self.success_dict[headers[0]] = timestamp
        self.success_dict[headers[1]] = application_name
        self.success_dict[headers[2]] = description
        self.success_dict[headers[3]] = status
        success_values.append(self.success_dict)
        return success_values


class Warning:
    warning_dict = {}

    def __init__(self, timestamp='01-01-2000', application_name='app_name',
                 description='description', status='Warning'):
        self.timestamp = timestamp
        self.application_name = application_name
        self.description = description
        self.status = status

    def read_log_file(self):
        with open(file_path + '\\log.csv', 'r') as log:
            for i in log:
                if 'Warning' in i and 'Failed' not in i:
                    print(i)

    def set_log_data(self, timestamp='01-01-2000', application_name='app_name',
                     description='description', status='Warning'):
        warning_values = []
        self.warning_dict[headers[0]] = timestamp
        self.warning_dict[headers[1]] = application_name
        self.warning_dict[headers[2]] = description
        self.warning_dict[headers[3]] = status
        warning_values.append(self.warning_dict)
        return warning_values


class Session:
    session_dict = {}

    def __init__(self, timestamp='01-01-2000', application_name='app_name',
                 description='description', status='Session'):
        self.timestamp = timestamp
        self.application_name = application_name
        self.description = description
        self.status = status

    def read_log_file(self):
        with open(file_path + '\\log.csv', 'r') as log:
            for i in log:
                if 'Session' in i:
                    print(i)

    def set_log_data(self, timestamp='01-01-2000', application_name='app_name',
                     description='description', status='Session'):
        session_values = []
        self.session_dict[headers[0]] = timestamp
        self.session_dict[headers[1]] = application_name
        self.session_dict[headers[2]] = description
        self.session_dict[headers[3]] = status
        session_values.append(self.session_dict)
        return session_values


all_log = open(file_path + '\\log.csv', 'w')
failed = Failed()
success = Success()
warning = Warning()
session = Session()
with open(file_path + "\\log.txt", "r", newline='') as log:
    write_file = csv.DictWriter(all_log, fieldnames=headers)
    write_file.writeheader()
    for i in log:
        if 'Failed' in i:
            write_file.writerows(
                failed.set_log_data(i[:19], i[43: 46], i[50:i.index('[')], code=i[i.index('['):i.index(']') + 1]))
    log.seek(0)
    for j in log:
        if 'Success' in j:
            write_file.writerows(success.set_log_data(j[:19], j[43: 46], j[50:]))
    log.seek(0)
    for k in log:
        if 'Warning' in k and 'Failed' not in k:
            write_file.writerows(warning.set_log_data(k[:19], k[43: 46], k[50:]))
    log.seek(0)
    for l in log:
        if 'Session' in l:
            write_file.writerows(session.set_log_data(l[:19], l[43: 46], l[50:]))
all_log.close()
failed.read_log_file()
success.read_log_file()
warning.read_log_file()
session.read_log_file()
