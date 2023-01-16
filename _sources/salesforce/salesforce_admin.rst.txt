Salesforce admin [#]_
=====================

.. contents::
    :depth: 1
    :local:
    :backlinks: entry

Learn About the Salesforce Admin Role
-------------------------------------

Salesforce Administration is an operational role. Salesforce Admins solve business problems by customizing the Salesforce Platform. They build, configure, and automate techonology solutions to deliver business value. Core responsibilities include supporting users, managing data, maintaining security standards, and delivering actionable analytics.

Required Skills
...............

Communication:
  Collaborate with busines and technical stakeholders to design, configure, adn implement Salesforce.
Problem solving: 
  Solve business problems using the Salesforce Platform. Helps being ``detail-oriented`` and to have ``analytical skills``.
Security management: 
  Proactively set up processes to manage and protect customer and business data.
Data analysis:
  Provide reporting on a regular basis to help users and executives gain insights and make decisions from Salesforce data.
Designer's mindset:
  Create huma-centered user experiences in Salesforce.
Process automation:
  Create, maintain, and enhance automated business processes.
Project management:
  Plan and overse Salesforce projects to ensure they're completed on time and within budget.

Key Responibilites
..................

User Management:
  The Salesforce Admin serves as a subject matter expert for user and team needs. They desing a Salesforce solution that is customized and ensures a good user experience. Behind this is the goal to ``improve productivity`` and ``increase adoption``.

Data Management:
  Salesforce Admins use their expertise to ``ensure the data is high quality`` (no duplications), that the data can be reported on for key business decisions, and that ``users get the information they need easily``.

Security:
  The Salesforce Admin collaborates with the company's IT and security teams to ensure the Salesforce solution aligns with compliance needs and policies. The admin ensures Salesforce is configured so that users see only what they need to see.

Actionable Analytics:
  The Salesforce Admin takes building reports a step further by ensuring the reports and dashboards built for their company are ``easy to read`` an that users can ``make critical decisions based on the information they're seeing``.

Essential Habits for Salesforce Admins
--------------------------------------

`Create your own Calendar Habits Kit <https://org62.my.salesforce.com/sfc/p/#000000000062/a/3y000001UL0V/vMgMiOnP9L.5hI5AY544xrCLLyxbwt9Tp0_PYH.Ym3A>`_

1. User management
..................

- Observe your users (30 min per week).
- Review and report on adoption (60 min per week).

  - Perform user audits

- Communicate with stakeholders (60 min per month).
- Create and maintain a user guide (60 min per week).

  - Each function
  - Other admins
  - Descriptions, Help Text, and In-Apss Guidance

.. admonition:: Summary

  Gather information on ``MON`` or ``TUE``, study what we have and how well we are using it on ``WED`` or ``THU``, and on ``THU`` or ``FRI`` add documentation.

2. Data management
..................

- Create and maintain backup solution (30 min per month).

  - Weekly data export.

    - Include images, documents, attachments.

- Cleanse data (time estimation depends on the project).

  - Create a custom report type (object + DUPLICATES).
  - Workflow rules, process builder, flow.

- Review and refresh sandboxes (30 min per week).

  - Good idea to ensure the sandboxes are refreshed after each successful production deployment.
  - Do not refresh before talking to the sandbox's owner.

- Maintain and improve your org (time estimation depends on the project).

  - **Don't configure directly in production**.
  - Focus on the most important areas for your business.
  - Run Optimizer for an overview of where to begin.
  - Run Lightning Page Optimization for specific performance recommendations.

- Maintain your Data Dictionary (60 min per week).

  - Data type & attributes (length)
  - API name
  - Sample result
  - Business purpose
  - Integrations or Dependencies
  
  (Try the nonprofit starter pack `data dictionary template <sforce.co/NPSPDataDictionary>`_)

.. admonition:: Summary

  On ``MON`` or ``TUE`` solicit feedback and observe users. Design and configure solutions on ``WED`` or ``THU``, and communicate and deploy changes on ``THU`` or ``FRI``.

3. Security
...........

- Managing communication with partners and IT (60 min per week).

  - Compliance policies
  - User onboarding and off-boarding procedures
  - Updates to data structures for integrations (data dictionaries)
  - Sandbox provisioning
  - Automated scripts
  - Multifactor authentication

- Review access and visibility on users (60 min per week).

  - 4 layers controls access and visibility:

    .. hint::

      Compile access related notes each week and organize them according this 4 layers.

    1. Organization:

      .. hlist::

        - Single sign-on
        - Multi-factor authentication
        - Password policies
        - Certificate & key management

    2. Persona:
        
    .. hlist::

      - Profile
      - Permission sets
      - Permission set groups
      - IP restrictions & login hours

    3. Record:
        
    .. hlist::

      - OrgWide defaults
      - Sharing rules, sets & groups
      - Role hierarchy
      - Manual & programmatic sharing
      - Teams
      - Territories
        
    4. Field:

    .. hlist::

      - Field level security

- Run Health Check:

  - Measure your Org's security against Salesforce's standard baseline.
  - Easily identify at-risk security settings.
  - Fix with one click for immediate results.
  - Customize based on your company's compliance needs.

- Stay up to date on security features (learn continuously at leat 60 min per week):

  - Visit Salesforce security websites:

    * trust.salesforce.com/en/security
    * admin.salesforce.com/security

  - Subscribe to the Admin Digest.
  - Read latest release notes security section.
  - Activate security-focused release updates in Setup.

.. admonition:: Summary

  Deepening knowledge on security early on the week ``TUE``. Review access and visibility for users on ``WED``, and communicate with IT on ``FRI``.

----

- Salesfroce:

  - Provide solutions that enable the customer to keep their data secure.
  - Educate customers on the need for security and how to enable it.

- Admin:

  - Adopt evolving security controls and features.
  - Continually monitor user behaviors and event logs.
  - Protect sensitive data in alignment with compliance standards.

----

.. important::

  - Salesforce releases 3 updates each year.
  - Ensure users have the least level of access to the system and data necessary to perform their job functions.
  - Users have access to applications, objects, fields and pages their required.


4. Actionable analytics
.......................

Actionable analytics allow your company to drive business decisions by using your Salerfoce data.

- Conduct quarterly Business Review ``QBR`` (several hours per quarter).

  - Business reviews are meetings in which business leaders and individual contributors discuss business goals and the progress they've made so far.
  - You are there to listen and observe.
  - Take notes about complaints and wins, and how well your org is configured to assist in those plans.

- Confirm and update KPIs (1 hour per quarter).

- Review and update key reports and dashboards (few hours per quarter / after KPIs).

  - Document reporting changes and related business initiatives.
  - Explain changes to how KPIs are masured.
  - Share pain points that have been removed.
  - Communicate across multiple messaging channels.
  - Include a method to capture feedback and questions.

.. admonition:: Summary

  Quaterly Business Review ``MON``, confirm KPIs ``TUE`` and review reports and dashboards ``WED``. (Once a quarter)

Salesforce Platform Basics
--------------------------

APP: 
  A set of objects, fields, adn other functionality that supports a business process. (switch between apps using the APP Launcger a.k.a. the waffle).
Objects: 
  Tables in the Salesforce database that sotre a particular kind of information. There are ``standard objects`` like Accounts and Contacts and ``custom objects``.
Records:
  Rows in object database tables. Records are the actual data assotiated with an object.
Fields:
  Columns in object database tables.
Org: 
  A specific instance of Salesforce.

Trailhead Playground (TP)
.........................

A safe environment where you can practice the skills you're learning before you take them to your real work. You can have up to 10 at a time.

Customizing the Salesforce Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Developing without code is known as no-code (or declarative) development. With no-code development, you use forms and drag-and-drop tools to perform powerful customization tasks. The platfomr also offers ``programmatic development``, which uses things like Lightning components.

Every time you create a custom objecto, you automatically get something called ``Chatter`` feed tracking. As you start building with the platform, keep your eye out for process with:
  
  - Heavy email collaboration
  - Reliance on spreadsheets
  - Shared local documents
  - Time-intensive, repetitive manual steps
  - Impact on only a few departments (you want to minimize the number of stakeholders while you're still learning)

  Processes with these traits are great candidates for early projects on the Salesforce platform.

Understand the Salesforce Architecture
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Salesforce is a cloud company. Everything we offer resides in the trusted, multitenant cloud.
* The Salesforce platform is the foundation of our services. It's powered by metadata and made up of different parts, like data services, artificial intelligence, and a robust APIs for development.
* All our apps sit on top of the platform. Our prebuilt offerings like Sales Cloud and Marketing Cloud, along with apps you build using the platform, have consistent, powerful functionality.
* Eveything is integrated. Our platform tehcnologies like predictive analytics and the development framework are built into everything we offer and everything you build.



Glossary
--------

.. glossary::
  
  Add custom field to std object
    :menuselection:`Setud --> Object Manager --> Object --> Details panel: Fields & Relationships --> New

  Use :term:`Add custom field to std object`





.. [#] `Build Your Admin Career on Salesforce <https://trailhead.salesforce.com/es-MX/users/strailhead/trailmixes/build-your-admin-career-on-salesforce>`_
