import sys, logging
import mechanize

logger = logging.getLogger("mechanize")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.DEBUG)

browser = mechanize.Browser()
browser.set_debug_http(True)
browser.set_debug_responses(True)
browser.set_debug_redirects(True)

url = "https://passport2.peralta.edu/psp/EPAPROD/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL?PORTALPARAM_PTCNAV=HC_CLASS_SEARCH_GBL3&EOPP.SCNode=EMPL&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=PCC_STUDENT_SERVICES&EOPP.SCLabel=Schedule%2520of%2520Classes&EOPP.SCFName=PCC_F200805080614503884090701&EOPP.SCSecondary=true&EOPP.SCPTcname=PT_PTPP_SCFNAV_BASEPAGE_SCR&FolderPath=PORTAL_ROOT_OBJECT.PORTAL_BASE_DATA.CO_NAVIGATION_COLLECTIONS.PCC_STUDENT_SERVICES.PCC_F200805080614503884090701.PCC_S200805080615252087771233&IsFolder=false"

response = browser.open(url)
