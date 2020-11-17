from newrelic.agent import NewRelicContextFormatter
import newrelic.agent
import logging
from django.http import HttpResponse

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': './debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
        # Uncomment the following snippet to prevent 
        # the logger from picking up the Python agent logs
        # },
        # 'newrelic': {
        # 	'level': 'NOTSET',
        # 	'propagate': False
        # }
    }
})

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

# NR Logging
handler = logging.StreamHandler()
formatter = NewRelicContextFormatter()
handler.setFormatter(formatter)
root_logger = logging.getLogger()
root_logger.addHandler(handler)

def index(request):
    # It's expected to see an initial [] logged due to the Python agent activation. 
    # Subsequent requests will generate headers.
	headers = []
	transaction = newrelic.agent.current_transaction()
	if transaction:
		newrelic.agent.insert_distributed_trace_headers(headers)
	logger.info("NR Headers %s", headers)
	return HttpResponse("Hello logging world.")