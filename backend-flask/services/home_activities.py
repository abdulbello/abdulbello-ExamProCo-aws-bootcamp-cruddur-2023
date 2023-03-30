from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import db


tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run(cognito_user_id=None):
    #Honeycomb
    #with tracer.start_as_current_span("home-activities-mock-data"):
      #span = trace.get_current_span()
      #now = datetime.now(timezone.utc).astimezone()
      #span.set_attribute("app.now", now.isoformat())
#tracer = trace.get_tracer("home.activities")
    #logger.info("HomeActivities")
    #with tracer.start_as_current_span("home-activites-mock-data"):
    #  span = trace.get_current_span()
    #  now = datetime.now(timezone.utc).astimezone()
    #  span.set_attribute("app.now", now.isoformat())
    
    sql = db.template('activities','home')
    results = db.query_array_json(sql)
    return results


      #if cognito_user_id != None:
        #extra_crud = {
          #'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
          #'handle':  'Lore',
          #'message': 'My dear brother, it the humans that are the problem',
          #'created_at': (now - timedelta(hours=1)).isoformat(),
          #'expires_at': (now + timedelta(hours=12)).isoformat(),
          #'likes': 1042,
          #'replies': []
        #}
        #results.insert(0,extra_crud)


      #xray/Cloudwatch --
      #logger.info("home activities")

      #Honeycomb
      #span.set_attribute("app.result_length",len(results))
      #span.set_attribute("app.handle", HomeActivities().get_handles(results))
        
    return results


  def get_handles(self,results_:list()):
    handles_ = []
    for dict_ in results_:
      handle = dict_["handle"]
      handles_.append(handle)
      return handles_