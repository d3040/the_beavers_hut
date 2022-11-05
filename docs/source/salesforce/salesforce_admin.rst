Salesforce admin
================

[#]_

.. contents::
    :depth: 1
    :local:
    :backlinks: entry

Essential Habits for Salesforce Admins
--------------------------------------

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

.. note::

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

.. note::

  On ``MON`` or ``TUE`` solicit feedback and observe users. Design and configure solutions on ``WED`` or ``THU``, and communicate and deploy changes on ``THU`` or ``FRI``.

3. Security
...........

- Salesfroce:

  - Provide solutions that enable the customer to keep their data secure.
  - Educate customers on the need for security and how to enable it.

- Admin:

  - Adopt evolving security controls and features.
  - Continually monitor user behaviors and event logs.
  - Protect sensitive data in alignment with compliance standards.

- Salesforce releases 3 updates each year.
- Ensure users have the least level of access to the system and data necessary to perform their job functions.
- Users have access to applications, objects, fields and pages their required.

- Managing communication with partners and IT (60 min per week).

  - Compliance policies
  - User onboarding and off-boarding procedures
  - Updates to data structures for integrations (data dictionaries)
  - Sandbox provisioning
  - Automated scripts
  - Multifactor authentication

- Review access and visibility on users.

  - 4 layers controls access and visibility:

  .. hint::

    Compile access related notes each week and organize them according this 4 layers.

    #. Organization:
      Single sign-on, Multi-factor authentication, password policies, certificate & key management.
    #. Persona:
      Profile, permission sets, permission set groups, IP restrictions & login hours.
    #. Record
      OrgWide defaults, sharing rules, sets & groups, role hierarchy, manual & programmatic sharing, teams, territories.
    #. Field:
      Field level security.

- Stay up to date on security features (learn continiously).

.. note::

  On ``MON`` or ``TUE`` solicit feedback and observe users. Design and configure solutions on ``WED`` or ``THU``, and communicate with IT on ``FRI``.



4. Actionable analytics
.......................


.. [#] `Build Your Admin Career on Salesforce <https://trailhead.salesforce.com/es-MX/users/strailhead/trailmixes/build-your-admin-career-on-salesforce>`_
