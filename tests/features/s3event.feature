Feature: The AWS Lambda function s3event

  Scenario Outline: a file is uploaded to a bucket
    Given we have a bucket named "<source>"
    When anyone uploads an image file "<image>" to "<source>"
    Then the file "<output>" is written to "<target>"
    And the contents are "<mimetype>"

  Scenario: upload HappyFace.jpg to tuple-source
    Given we have a bucket named "tuple-source"
    When anyone uploads an image file "HappyFace.jpg" to "tuple-source"
    Then the file "s3event_output.txt" is written to "tuple-target"
    And the contents are "image/jpg"
 