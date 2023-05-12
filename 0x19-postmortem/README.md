0x19. Postmortem
DevOps
SysAdmin


On-call

Being on-call
(of a person) able to be contacted in order to provide a professional service if necessary, but not formally on duty.

“our technicians are on call around the clock”

synonyms: on duty, on standby, available

“Dr. Merton is on call this evening”


-Google
Users and consumers expect their favorite websites and services to be constantly accessible. Have you ever seen Facebook, Amazon, LinkedIn, Ebay down? Probably not. Any downtime means users frustration and potentially millions of dollars in loss. That’s true for the big players but also for any company where its online presence is crucial, which is the case for a lot of businesses.

This does not happen magically. Software engineers are building reliable systems that are supposed to be up and running 100% of the time, but sometimes things go sideways and the issue needs to be fixed as soon as possible. To achieve quick resolution time, companies are putting in place monitoring systems to detect any anomaly and alert the employee who is on-call. This sometimes happens during working hours, but also at 3am or at night.


Setup
To be on call you need at least 4 components:
A service or website you want to monitor
A monitoring tool
An oncall management system
A software engineer (that’s you)


A service or website you want to monitor
You can monitor thousands of things:
Is my website returning HTTP 200?
Is my website loading in less than 500ms?
Is my webserver daemon up?
Is there more than 50% free disk space on my server?



A monitoring tool
You need to configure one or multiple monitoring tool(s) to your on-call system, they are the ones that will actually detect any anomaly and report it to the on-call platform. Check out the Monitoring concept page for recommandations.




A on-call management system
A lot of home tools can be used for that, you can for example in Nagios define on-call periods and then hook this up to a 3rd party service that can send a text message for you. This is fine when you are alone on-call but become very complicated when you have a team. That’s what a company started in 2009 is doing in the Cloud: PagerDuty. It’s a service that allows you to define on-call teams, escalation policies and services integration.



On-call management system flow
Let’s get a bit more into detail about the flow of an on-call management system such as PagerDuty. First of all you have to understand that PagerDuty is not monitoring your website, it acts as a gateway between your monitoring tools and the software engineers that are on-call. Its goal is to alert, as soon as possible, as reliably as possible and as efficiently as possible the person or team on-call. That’s a very hard duty because if PagerDuty goes down then many sites or services going down at the same time won’t be fixed because the alerts won’t reach the on-call persons.

Let’s get into a simple and typical workflow: 1. An incident has been detected by an external monitoring tool that notifies PagerDuty. 2. PagerDuty creates an incident and assigns it to the on-call person, the alert is in a “triggered” mode. 3. The on-call person gets notified and acknowledges the alert meaning that the software engineer is looking into the problem. 4. If the engineer cannot solve the issue, she/he can escalate it (pass it on) to another co-worker. PagerDuty also allows automatic escalation in case the on-call person does not acknowledge the alert (which means that for some reason the on-call person is not available - no battery on the phone, not hearing the ringtone and all sorts of good stuff :-)) 5. A brilliant software engineer (most likely a ALX School member) solves the issue and marks the incident as solved. Depending on the type of alert and service that notified PagerDuty, it can be auto-resolved.


On-call teams are usually rated on 2 metrics:
MTA (Medium Time to Acknowledgement): The time between an alert/incident is created and an on-call person acknowledged it (which means that he or she is working toward a solution)
MTR (Medium Time to Resolution): The time between an alert/incident being created and this same incident/alert being marked as solved

You obviously want these mean times to be as low as possible. MTA basically tells how good engineers are at answering their phone. MTR basically tells how good engineers are at solving issues.




PagerDuty
We made a partnership so that Holberton School students can utilize PagerDuty for free. For every student a team is created (team of one), we will also have teams for group projects later on.

Every PagerDuty team has an automatically created and linked: - Escalation policy - Services (which are monitoring tools, we can add more services upon demand to Holberton School staff)

We advise you to create accounts with the recommended monitoring tools and to connect them with PagerDuty using the pre-created services.

Also make sure to configure your profile to fill in your contact information and define the Notification Rules


POSTMORTERM
a postmortem is a retrospective analysis or review of an incident or outage that occurred in the system or application.

The goal of a postmortem is to identify the root cause of the incident, document the steps taken to resolve it, and identify ways to prevent similar incidents from occurring in the future.

During a postmortem, the team involved in incident response reviews the events leading up to the incident, the actions taken to resolve it, and any remediation steps that may need to be taken. The review typically includes a detailed analysis of the system logs, monitoring data, and other relevant information to identify the underlying cause of the incident.

The findings of a postmortem are typically documented in a report or analysis that outlines the root cause of the incident, the steps taken to resolve it, and any recommendations for improving the system to prevent similar incidents in the future. The report may also include a list of action items that need to be completed to address any identified deficiencies or weaknesses in the system.


In general, an effective postmortem report tells a story. Incident postmortem reports should include the following:
Issue Summary: A brief overview of the incident, including the duration of the outage, the impact on the system or application, and the percentage of users affected.

Timeline: A detailed timeline of the incident, including when the issue was detected, how it was detected, and the actions taken to resolve it. This should also include any misleading investigation paths that were taken and how the incident was escalated.

Root Cause and Resolution: A detailed explanation of the root cause of the incident and how it was resolved. This should also include any corrective and preventative measures that were taken to prevent similar incidents from occurring in the future.

Corrective and Preventative Measures: A list of action items that need to be completed to address any identified deficiencies or weaknesses in the system. This should be very specific, like a TODO list, and include tasks such as patching servers, adding monitoring on server memory, and reviewing load balancer configurations.

Lessons Learned: A summary of the lessons learned from the incident, including what worked well and what didn't work well. This should also include any recommendations for improving the incident response process or the system itself.

Conclusion: A brief summary of the postmortem report, including any key takeaways or next steps.

Postmortem reports should be written in clear and concise language, and should be reviewed by all team members involved in the incident response process. The report should be shared with relevant stakeholders, including senior management and customers, if necessary.

