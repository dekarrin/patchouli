from pytelegrafhttp.util import check_online

# Global default install directory for all files. Note that each specific file / directory may override where it is
# located, but by default they are all grouped together
install_dir = '/etc/pytelegrafhttp'


###############
# ENVIRONMENT #
###############

# Directory for files for use with daemon communication
env_daemon_files_dir = install_dir + '/daemon'

env_cookies_file = install_dir + '/cookies.pkl'

env_state_file = install_dir + '/state.pkl'


########
# TIME #
########

# How often metrics are collected. Measured in seconds.
time_collection_interval = 120

time_save_frequency = 5


###########
# LOGGING #
###########

# Location of log file directory (by default all logs are kept together; override individual log file paths to change
# this).
log_dir = install_dir + '/logs'

# Location of log file that contains all output
log_main_log_path = log_dir + '/main.log'

# Location of log file that contains only errors
log_error_log_path = log_dir + '/errors.log'

# Maximum size of a log file before it is rotated. Format is flexible, and accepts strings such as "24KB", "8g", or
# "5kbs"
log_file_max_size = "5 Mbs"

# Number of log files to keep. Once this number of rotated logs is reached, every rotation after that will cause the
# oldest one to be deleted.
log_file_keep_count = 4

# Additional system log to use. Adding one of these values requires that the associated python module is installed on
# the host system separately from this application.
#
# Supported values are: 'systemd'
log_os_logs = []
# Uncomment to enable journalctl logging
log_os_logs.append('systemd')


###########
# SCRAPER #
###########

scraper_host = 'e-hentai.org'
scraper_username = 'yourusername'
scraper_password = 'XXXXXXXXXX'
scraper_use_ssl = True
scraper_login_steps = [
        ('attempt', {'endpoint': '/hentaiathome.php'}),
        ('resp-extract', {'type': 'form-vars', 'inject': {'UserName': 'username', 'PassWord': 'password'}}),
        ('submit-form', {}),
        ('bounce-transfer', {'pattern': '<a href="([^"]+)">Or click here if you do not wish to wait</a>'}),
        ('verify', {'pattern': 'H@H Miss% shows the percentage of requests'})
]
scraper_bot_kicked_pattern = 'banned for excessive pageloads which indicates'
scraper_logged_out_pattern = 'requires you to log on.</p>'
scraper_telegraf_destinations = {
        'hath-client-net-stats': {
                'port': 10050,
                'global-tags': {}
        },
        'hath-net': {
            'port': 10051,
            'global-tags': {}
        }
}
scraper_endpoints = []
scraper_endpoints.append({
        'endpoint': '/hentaiathome.php',
        'verify-pattern': 'H@H Miss% shows the percentage of requests',
        'metrics': [
                {
                        'dest': 'hath-net',  # destination db / telegraf identifier
                        'name': 'hath_net',  # metrics name
                        'regex': [
                                r'<td>North and South America</td>\s*',
                                r'<td [^>]*>[^ ]+ Gbit/s</td>\s*',
                                r'<td [^>]*>=</td>\s*',
                                r'<td [^>]*>([^ ]+) MB/s</td>\s*',
                                r'<td [^>]*>([^ ]+) %</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>',
                        ],
                        'values': [
                                {'name': 'load', 'conversion': int, 'type': 'CAPTURE-1'},
                                {'name': 'miss-rate', 'conversion': float, 'type': 'CAPTURE-2'},
                                {'name': 'coverage', 'conversion': float, 'type': 'CAPTURE-3'},
                                {'name': 'hits-per-gb', 'conversion': float, 'type': 'CAPTURE-4'},
                                {'name': 'quality', 'conversion': int, 'type': 'CAPTURE-5'}
                        ],
                        'tags': {'region': 'americas'}
                },
                {
                        'dest': 'hath-net',
                        'name': 'hath_net',
                        'regex': [
                                r'<td>Europe and Africa</td>\s*',
                                r'<td [^>]*>[^ ]+ Gbit/s</td>\s*',
                                r'<td [^>]*>=</td>\s*',
                                r'<td [^>]*>([^ ]+) MB/s</td>\s*',
                                r'<td [^>]*>([^ ]+) %</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>',
                        ],
                        'values': [
                                {'name': 'load', 'conversion': int, 'type': 'CAPTURE-1'},
                                {'name': 'miss-rate', 'conversion': float, 'type': 'CAPTURE-2'},
                                {'name': 'coverage', 'conversion': float, 'type': 'CAPTURE-3'},
                                {'name': 'hits-per-gb', 'conversion': float, 'type': 'CAPTURE-4'},
                                {'name': 'quality', 'conversion': int, 'type': 'CAPTURE-5'}
                        ],
                        'tags': {'region': 'europe-africa'}
                },
                {
                        'dest': 'hath-net',
                        'name': 'hath_net',
                        'regex': [
                                r'<td>Asia and Oceania</td>\s*',
                                r'<td [^>]*>[^ ]+ Gbit/s</td>\s*',
                                r'<td [^>]*>=</td>\s*',
                                r'<td [^>]*>([^ ]+) MB/s</td>\s*',
                                r'<td [^>]*>([^ ]+) %</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>',
                        ],
                        'values': [
                                {'name': 'load', 'conversion': int, 'type': 'CAPTURE-1'},
                                {'name': 'miss-rate', 'conversion': float, 'type': 'CAPTURE-2'},
                                {'name': 'coverage', 'conversion': float, 'type': 'CAPTURE-3'},
                                {'name': 'hits-per-gb', 'conversion': float, 'type': 'CAPTURE-4'},
                                {'name': 'quality', 'conversion': int, 'type': 'CAPTURE-5'}
                        ],
                        'tags': {'region': 'asia-oceania'}
                },
                {
                        'dest': 'hath-net',
                        'name': 'hath_net',
                        'regex': [
                                r'<td>Global</td>\s*',
                                r'<td [^>]*>[^ ]+ Gbit/s</td>\s*',
                                r'<td [^>]*>=</td>\s*',
                                r'<td [^>]*>([^ ]+) MB/s</td>\s*',
                                r'<td [^>]*>([^ ]+) %</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td [^>]*>([^<]+)</td>',
                        ],
                        'values': [
                                {'name': 'load', 'conversion': int, 'type': 'CAPTURE-1'},
                                {'name': 'miss-rate', 'conversion': float, 'type': 'CAPTURE-2'},
                                {'name': 'coverage', 'conversion': float, 'type': 'CAPTURE-3'},
                                {'name': 'hits-per-gb', 'conversion': float, 'type': 'CAPTURE-4'},
                                {'name': 'quality', 'conversion': int, 'type': 'CAPTURE-5'}
                        ],
                        'tags': {'region': 'global'}
                },
                {
                        'dest': 'hath-client-net-stats',
                        'name': 'hath_health',
                        'regex': [
                                r'<tr>\s*',
                                r'<td><a [^>]*>([^<]+)</a></td>\s*',
                                r'<td>([^<]+)</td>\s*',
                                r'<td [^>]*>Online</td>\s*',
                                r'<td>[^<]*</td>\s*',
                                r'<td>([^<]*)</td>\s*',
                                r'<td>([^<]+)</td>\s*',
                                r'<td [^>]*>[^<]+</td>\s*',
                                r'<td>[^<]*</td>\s*',
                                r'<td>[^<]*</td>\s*',
                                r'<td>[^<]*</td>\s*',
                                r'<td [^>]*>([^<]+)</td>\s*',
                                r'<td>([^<]+)</td>\s*',
                                r'<td>([^ ]+) / min</td>\s*',
                                r'<td>([^ ]+) / day</td>\s*',
                        ],
                        'values': [
                                {'name': 'online', 'conversion': lambda last: check_online(last, max_minutes=5), 'type': 'CAPTURE-3'},
                                {'name': 'files', 'conversion': lambda s: int(s.replace(',', '')), 'type': 'CAPTURE-4'},
                                {'name': 'trust', 'conversion': int, 'type': 'CAPTURE-5'},
                                {'name': 'quality', 'conversion': int, 'type': 'CAPTURE-6'},
                                {'name': 'hitrate', 'conversion': float, 'type': 'CAPTURE-7'},
                                {'name': 'hathrate', 'conversion': float, 'type': 'CAPTURE-8'}
                        ],
                        'tags': {
                                'host': 'CAPTURE-1',
                                'client-id': 'CAPTURE-2',
                        }
                },
                {
                        'dest': 'hath-client-net-stats',
                        'name': 'hath_health',
                        'regex': [
                                r'<tr>\s*',
                                r'<td><a [^>]*>([^<]+)</a></td>\s*',
                                r'<td>([^<]+)</td>\s*',
                                r'<td [^>]*>Offline</td>\s*',
                                r'<td>[^<]*</td>\s*',
                                r'<td>[^<]*</td>\s*',
                                r'<td>([^<]+)</td>\s*',
                                r'<td [^>]*>Not available when offline</td>\s*'
                        ],
                        'values': [
                                {'name': 'online', 'conversion': 0, 'type': 'VALUE'},
                                {'name': 'files', 'conversion': lambda x: int(x.replace(',', '')), 'type': 'CAPTURE-3'}
                        ],
                        'tags': {
                                'host': 'CAPTURE-1',
                                'client-id': 'CAPTURE-2',
                        }
                }
        ]
})
