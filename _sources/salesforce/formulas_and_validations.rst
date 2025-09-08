*******************************************************************************
Formulas and Validations [#]_
*******************************************************************************

.. contents::
   :depth: 1
   :local:
   :backlinks: entry

Use Formula Fields
==================

Example of creating a Costum Formula Field (e.g. Opportunity sum of opportunities from an account):

1. From Setup, open the `Object Manager` and click ``Opportunity``.
2. In the left sidebar, click ``Fields & Relationships``.
3. Click ``New``.
4. Select ``Formula`` and click `Next`.
5. In ``Field Label``, type *My Formula Field* (notice that Field Name populates automatically).
6. Select the type of data you expect your formula to return.
7. Click `Next`.

+------------+----------------------------+
| Operator   | Operation                  |
+============+============================+
| ``+``      | ADD                        |
+------------+----------------------------+
| ``-``      | Subtract                   |
+------------+----------------------------+
| ``*``      | Multiply                   |
+------------+----------------------------+
| ``/``      | Divide                     |
+------------+----------------------------+
| ``^``      | Exponentiation             |
+------------+----------------------------+
| ``(``      | Open Parenthesis           |
+------------+----------------------------+
| ``)``      | Close Parenthesis          |
+------------+----------------------------+
| ``&``      | Concatenate                |
+------------+----------------------------+
| ``=``      | Equal                      |
+------------+----------------------------+
| ``<>``     | Not Equal                  |
+------------+----------------------------+
| ``<``      | Less Than                  |
+------------+----------------------------+
| ``>``      | Greater Than               |
+------------+----------------------------+
| ``<=``     | Less Than or Equal         |
+------------+----------------------------+
| ``>=``     | Greater Than or Equal      |
+------------+----------------------------+
| ``&&``     | AND                        |
+------------+----------------------------+
| ``||``     | OR                         |
+------------+----------------------------+



Implement Roll-Up Summary Fields
================================

While formula fields calculate values using fields within a single record, roll-up summary fields calculate values 
from a set of related records, such as those in a related list. You can create roll-up summary fields that 
automatically display a value on a master record based on the values of records in a detail record. These detail 
records must be directly related to the master through a master-detail relationship.

Master-detail relationships closesly link objects together so that the master record controls specific behaviors of the
detail and subdetail record.

A roll-up summary field must be defined on the object that is on the master side of a master-detail relationship.

Example of creating the Summary Field (sum of opportunities from an account):

1. From Setup, open `Object Manager` and click ``Account``.
2. On the left sidebar, click ``Fields & Relationships``.
3. Click `New`.
4. Choose the `Roll-Up Summary` field type, and click `Next`.
5. For Field Label, enter ``Sum of Opportunities`` and click `Next`.
6. The Summarized Object is the detail object that you want to summarize. Choose `Opportunities`.
7. Choose the `SUM` Roll-up type and choose `Amount` as the Field to Aggregate. If you're unable to see Amount in Field
   to Aggregate, disable the Advanced Currency Management in your Currency Setup.
8. Click `Next`, `Next`, and `Save`.

Keep in mind that the types of fields you can calculate in a roll-up summary field depend on the type of calculation.
For example:

* Number, currency, and percent fields are available when you select `SUM` as the roll-up type.
* Number, currency, percent, date, and date/time fields are available when you select `MIN` or `MAX` as the roll-up
  type. 



Creating Validation Rules
=========================

Validation rules verify that data entered by users in records meets the standards you specify, by using formulas or
expressions, before they can save it. When the validation rule returns a value of `True`, this confirms that the data
entered by the user contains an invalid value. They can also include error messages to display to users when they enter
invalid values based on specified criteria. Using these rules effectively contributes to quality data.

Validation rules can be created for objects, fields, campaign members, or case milestones.

Example of creating a Validation Rule:

1. From Setup, go to `Object Manager` and click ``Account``.
2. In the left sidebar, click ``Validation Rules``.
3. Click `New`.
4. Enter the following properties for your validation rule:

   - Rule Name: Account_Number_8_Characters
   - Error Condition Formula: LEN( AccountNumber) <> 8

5. Error Message: Account number must be 8 characters long.
6. To check your formula for errors, click `Check Syntax`.
7. Click `Save` to finish.


.. [#] `Formulas and Validations <https://trailhead.salesforce.com/content/learn/modules/point_click_business_logic?trailmix_creator_id=d3040&trailmix_slug=d3040>`_
