import time
from odoo import api, fields, models


class ConnectorJob(models.Model):
    _name = "integration.connector.job"

    name = fields.Char(required=True)
    state = fields.Selection([("pending", "Pending"), ("done", "Done"), ("failed", "Failed")], default="pending")
    retries = fields.Integer(default=0)
    last_error = fields.Text()

    @api.model
    def run_with_retry(self, job, sender, max_retries=4):
        delay = 1
        for attempt in range(max_retries + 1):
            try:
                sender(job)
                job.write({"state": "done", "last_error": False})
                return True
            except Exception as exc:
                job.write({"retries": attempt + 1, "last_error": str(exc)})
                if attempt >= max_retries:
                    job.write({"state": "failed"})
                    return False
                time.sleep(delay)
                delay = min(delay * 2, 16)
        return False
