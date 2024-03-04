from datetime import datetime

from marshmallow import Schema, fields, post_load, ValidationError

from logo.helpers import LogLevel, TIME_FORMAT, is_valid_ip


# Can also be done with marshmallow schem just didn't have time to replace it :(


def validate_ip(ip: str):
    if is_valid_ip(ip):
        raise ValidationError('Please provide a valid ip address!')


def validate_port(port: int):
    if 1 <= port <= 65535:
        raise ValidationError('Please provide a valid port!')


class LogMessageSchema(Schema):
    message = fields.Str(data_key='message', required=True)
    log_level = fields.Str(data_key='logLevel', required=False, missing=LogLevel.INFO.value)
    log_service_port = fields.Integer(data_key='logServicePort', required=False, validate=validate_port)
    log_service_address = fields.Str(data_key='logServiceAddress', required=False, validate=validate_ip)

    @post_load
    def add_log_timestamp(self, data, **kwargs):
        data['timestamp'] = datetime.now().strftime(TIME_FORMAT)
        return data
