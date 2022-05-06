import codecs
plain_text = "test"

cypher_text = codecs.encode(plain_text, 'rot_31')

print(cypher_text)

#Start decrypt rot_13

pico_text = "H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_AJ8H7JJ7"

decode_pico = codecs.decode(pico_text, 'rot_31')
print(decode_pico)
