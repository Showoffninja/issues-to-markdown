---
name: IT change
about: create an IT change
title: "IT Change: "
labels: IT Change
assignees: ""
---

# Immuta IT change

**ServiceNow Business Application:** 14659

**IT change category:** `Normal/Emergency`

## What will be changed

`Must describe the change.`

## Assessments

Determine if IT QA approval of implementation, release, and close of the IT change is required:

- **Does the IT change alter the intended use?** `Yes/No`
- **Does the IT change impact gross risk?** `Yes/No`
- **Does the IT change replace any supplier or their product?** `Yes/No`

Note: IT QA approval is required if one or more of these questions are answered by “Yes”.

- **Does the IT change alter a healthcare-regulated process, or can it alter GxP data?** `Yes/No`

## Implementation plan:

The solution is qualified according to “Manage IT Infrastructure” (QualityDocs Q216301). The following activities have been deemed commensurate to ensure fitness of intended use of the solution

1. Approve this IT change for implementation by Solution Owner or delegate by changing its status to “In Progress”.
2. If required according to above assessment, approve this IT change for implementation by IT QA by adding a comment to the IT change.
3. Update and attest IT Risk Assessment (if needed).
4. Update requirements and verification test cases in feature files (if needed).
5. Update design specifications and configuration specifications as markdown files (if needed).
6. Update Operating and Maintenance description (if needed).
7. Update user guides (if needed).
8. Implement the required changes to the solution using an agile approach.
9. Create a pull request linked to this IT change containing all changes to code and documentation.
10. Perform peer review and complete the pull request.
11. Execute verification through an [automated release pipeline](<(https://github.com/innersource-nn/o2-immuta/actions/workflows/main.yaml)>), which:
    - Builds the solution and deploys it to the validation environment.
    - Executes the test plan for the validation environment (see “Test Plan” below).
    - Deploys the solution to the production environment
    - Executes the test plan for the production environment (see “Test Plan” below).
12. Add close notes and approve this IT change for release and close by Solution Owner or delegate (always) and IT QA (if required according to assessment). IT QA approves by adding a comment to the IT change, while Solution Owner or delegate approves by changing its status to “Done”.

## Test plan:

_Test plan for validation environment_
The release pipeline performs the following activities as part of the verification in the validation environment:

1. Execute automatic IV test cases.
2. Wait for acknowledgement of execution of manual IV test cases, if any.
3. Wait for acknowledgement of execution of manual configuration, if any.
4. Execute automatic PV test cases (this includes regression tests).
5. Wait for acknowledgement of execution of manual PV test cases, if any.
6. Wait for creation of a manual test report of all manually executed test cases as a comment to the IT change. The manual test report must be authored by someone who is not Solution Owner or delegate.
7. Generate verification report including results of all automated test cases for the validation environment.
8. Wait for data review and approval of the verification report and the manual test report by Solution Owner or delegate. An immutable link to the manual test report is added as part of the approval of the verification report, along with a statement that the approval covers both the verification report and the manual test report, as well as data review of the latter. This releases the solution for the production environment.

_Test plan for production environment_
The release pipeline performs the following activities as part of the verification on the production environment:

1. Execute automatic pIV test cases.
2. Wait for acknowledgement of execution of manual pIV test cases, if any.
3. Wait for acknowledgement of execution of manual configuration, if any.
4. Execute automatic PV test cases (this includes regression tests). Note that the same PV test cases are executed on both the validation and the production environment.
5. Wait for acknowledgement of execution of manual PV test cases, if any.
6. Wait for creation of a manual test report of all manually executed test cases as a comment to the IT change. The manual test report must be authored by someone who is not Solution Owner or delegate.
7. Generate verification report including results of all automated test cases for the validation environment.
8. Wait for data review and approval of the verification report and the manual test report by Solution Owner or delegate. An immutable link to the manual test report is added as part of the approval of the verification report, along with a statement that the approval covers both the verification report and the manual test report, as well as data review of the latter. This releases the solution for the production environment.

## Close notes:

_<These close notes will be updated to fit the actual implementation before closing the IT change. Remember to ensure the IT change has a link to the final QMS Pipeline run (and add explanations for any partial runs), and a link to the pull request.>_
The following activities have been performed:

1. The IT change was approved for implementation.
2. IT Risk Assessment, requirements, verification test cases, design specifications, and configuration specifications were created/updated as needed (see link to pull request).
3. The required changes to the solution were implemented using an agile approach (see link to pull request).
4. The pull request was peer reviewed and completed (see link to pull request).
5. The verification was executed through an automated release pipeline, including building and deploying the solution to the validation and production environments and executing the corresponding test plans (see link to pipeline run).

All activities have been completed successfully, the application is fit for intended use, and thus the IT change is released for use when closing the change.

Note: The closer must remember to check that all development changes are correctly linked to this work item.
