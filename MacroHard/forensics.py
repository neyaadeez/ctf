import base64
hidden = '       Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q'
hidden = hidden.strip().replace(" ", "")
print("encoded String::{%s} ::" % hidden)
hidden = base64.b64decode(str(hidden+'==')).decode("utf-8")
print("decoded String:: {%s} ::"% hidden)