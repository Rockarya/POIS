Building secure MAC using PRF.

Take seed(in binary) and message(text) as input.

Algorithm:
Generate tag of the MAC for the sender using PRF. The tag is generated in same way as the encryption key(same as in q3). This will be called as sender's tag.
Use the reciver's binary message form to generate tag at reciver's end.
Send these both tags to Verify function. It returns verdict 'Accept' if the sender's tag and reciver's tag are same and 'Reject' in the other case.