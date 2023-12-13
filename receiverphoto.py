from dns_RD0 import build_message, send_udp_message, decode_message
import time
import base64
from io import BytesIO
from PIL import Image
from string import ascii_lowercase as alc


def decode_image(msg, output_path):
    try:
        # Decode base64-encoded image data
        image_binary = base64.b64decode(msg)

        # Create an in-memory binary stream for the image
        image_stream = BytesIO(image_binary)

        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_stream)

        # Save the image to the specified output path
        image.save(output_path)

        print(f"Image successfully decoded and saved to '{output_path}'.")
    except Exception as e:
        print(f"Error: {e}")


def receiver():
    msg = ""
    #offset = 0
    #t_end = time.time() + 60 * 0.5
    queries = ["0.iVBORw0KGgoAAAANSUhEUgAAAFcAAABTCAIAAABlOwwtAAAAAX.reddit.com",
    "1.NSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMA.reddit.com",
    "2.AA7DAcdvqGQAAAQCSURBVHhe7Zv/faowFEf1zVH3sIN0kDpI3a.reddit.com",
    "3.Pdo7pH2aPv0G/e/fCoQn4i0Zw/UkGE5OTmJkXcfn9/bx6eP+7v.reddit.com",
    "4.Y9Ms9DQLPc1CT7PQ0yz0NAs9zULPcqumruu+vr7O57OV7HHv/f.reddit.com",
    "5.D09PT8/MwLSl6/vLxo/xJgoSifn5+vr6+0yl0vEFy8v7+7cxWj.reddit.com",
    "6.VCzQz4fD4XQ6DTucTt7v97vdTuVIDUdyPC8+Pj6sNNCBTQVLfi.reddit.com",
    "7.QjI3T+MJhpKrUn/t3bIRAFfHZ4tkKhkdMCTR12LzWOa/xvaPnI.reddit.com",
    "8.Ba7deznIY4HWWi0RQaVztX/E29ubrgJc0e1NJoMFusVCgAB2e0.reddit.com",
    "9.vCVXQ5yDJAUi1Yhchbhfr/IsPoS1efZMHqQaC6XctiAyRxdERa.reddit.com",
    "10.oCtsFORNVKFwdVUjJRgjLWjeRsSSo+Aa1iXUyu0KJMbCqhSIRB.reddit.com",
    "11.HBFpQLVqVAmIiIHBFmwbLRbXPBNRCh6oVm6wALlodKrGFzYZUM.reddit.com",
    "12.6qcAC4q3ZdZFKWgJQ23dtge+FnTq6CS8MKEd5muBk8Kax8IQSx.reddit.com",
    "13.CeKdzLguaFxPXZwgTV2cvCj1ZfryshKBzmLSgj1BUIwj8c5i38.reddit.com",
    "14.CK0mIwxROPhMFjMWaDwnqjEQhCaL2bXDzPcRugWq0KqRw+FAeT.reddit.com",
    "16.w0EQC5T6puMaUxb0Sd1NqBf1YrwFRRERpc1K2e/3lOfzWZsXuf.reddit.com",
    "17.9Y0IiIz473EQs+TM2UtU+TxmxDpmLhcWgWeqYsKCNMrzfug/uP.reddit.com",
    "18.BZ8cP2XBZ45ZPz7z/ZQFn/XG+kmNBfkbPV9UHT6xMLVewKLPv6.reddit.com",
    "19.Urx2fVMzNHAC4UVHfMzBxR+6DwvTlAqEygr/2ICLddG2r/7K3j.reddit.com",
    "20.GQuAAk5EanDb9aBbx+C2rzMzIkCDQrcx60LDQd+nzOBsXMcmiL.reddit.com",
    "21.rCwarttifxOkiji9Jt10BQnb0sVBcO/hlB+B4X8WjEDVEuy//8.reddit.com",
    "22.Amiy8D/1rYjosAALcY8MLYyNhVLPNYE947bOBGH9VPAZN6HcS7.reddit.com",
    "23.ytTQT10ZiNmMuCLYByz6pEmALq5naFEGMBViUiUQFEWuDCEgG3.reddit.com",
    "24.TZaWC1K6JNKCUI6A0GyUC8vWEblgSJIFsP9VqMeSo2MYjOlLmF.reddit.com",
    "25.QLYFM0LLOmMvWMgizjMYMFYaMDCg0Q+h/jSoSQMfqyWQC6ZeiC.reddit.com",
    "26.11TavZcGrR2eOfvclNOCoOUjFwRwnA6aymet84GzlZiSSv3O+n.reddit.com",
    "27.Q6HY/H0W1b2VFJbhs2D7r/f5Q/fAaHIzmegTb6SDYkoxyj0AiC.reddit.com",
    "28.NhMLC6xHSsXCRQgNOlydTDn6moM27/79HP/ij/LLsaiF1TJ/D/.reddit.com",
    "29.oRaBZ6moWeZqGnWehpFnqahZ5mYbPZbP4CmCRMM6i8GFIAAAAA.reddit.com",
    "30.SUVORK5CYII=.reddit.com"]

    for query in queries:
        message = build_message("A", query)
        response = send_udp_message(message, "172.29.207.107", 9090)
        print(response)
        query_part = query.split(".")
        msg += query_part[1]
    print(queries)
    print(msg)
    msg = "iVBORw0KGgoAAAANSUhEUgAAAFcAAABTCAIAAABlOwwtAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAQCSURBVHhe7Zv/faowFEf1zVH3sIN0kDpI3aPdo7pH2aPv0G/e/fCoQn4i0Zw/UkGE5OTmJkXcfn9/bx6eP+7vY9Ms9DQLPc1CT7PQ0yz0NAs9zULPcqumruu+vr7O57OV7HHv/fD09PT8/MwLSl6/vLxo/xJgoSifn5+vr6+0yl0vEFy8v7+7cxWjVCzQz4fD4XQ6DTucTt7v97vdTuVIDUdyPC8+Pj6sNNCBTQVLfiQjI3T+MJhpKrUn/t3bIRAFfHZ4tkKhkdMCTR12LzWOa/xvaPnIBa7deznIY4HWWi0RQaVztX/E29ubrgJc0e1NJoMFusVCgAB2e0vCVXQ5yDJAUi1Yhchbhfr/IsPoS1efZMHqQaC6XctiAyRxdERaoCtsFORNVKFwdVUjJRgjLWjeRsSSo+Aa1iXUyu0KJMbCqhSIRBHBFpQLVqVAmIiIHBFmwbLRbXPBNRCh6oVm6wALlodKrGFzYZUM6qcAC4q3ZdZFKWgJQ23dtge+FnTq6CS8MKEd5muBk8Kax8IQSxCeKdzLguaFxPXZwgTV2cvCj1ZfryshKBzmLSgj1BUIwj8c5i38CK0mIwxROPhMFjMWaDwnqjEQhCaL2bXDzPcRugWq0KqRw+FAeTwetXmNmXvQ2+2WcvqYNdN1nW52W7K8yJ1/N0X7ARfgdl1iykLtw0EQC5T6puMaUxb0Sd1NqBf1YrwFRRERpc1K2e/3lOfzWZsXuf9Y0IiIz473EQs+TM2UtU+TxmxDpmLhcWgWeqYsKCNMrzfug/uPBZ8cP2XBZ45ZPz7z/ZQFn/XG+kmNBfkbPV9UHT6xMLVewKLPv6Urx2fVMzNHAC4UVHfMzBxR+6DwvTlAqEygr/2ICLddG2r/7K3jGQuAAk5EanDb9aBbx+C2rzMzIkCDQrcx60LDQd+nzOBsXMcmiLrCwarttifxOkiji9Jt10BQnb0sVBcO/hlB+B4X8WjEDVEuy//8Amiy8D/1rYjosAALcY8MLYyNhVLPNYE947bOBGH9VPAZN6HcS7ytTQT10ZiNmMuCLYByz6pEmALq5naFEGMBViUiUQFEWuDCEgG3TZaWC1K6JNKCUI6A0GyUC8vWEblgSJIFsP9VqMeSo2MYjOlLmFQLYFM0LLOmMvWMgizjMYMFYaMDCg0Q+h/jSoSQMfqyWQC6ZeiC11TavZcGrR2eOfvclNOCoOUjFwRwnA6aymet84GzlZiSSv3O+nQ6HY/H0W1b2VFJbhs2D7r/f5Q/fAaHIzmegTb6SDYkoxyj0AiCNhMLC6xHSsXCRQgNOlydTDn6moM27/79HP/ij/LLsaiF1TJ/D/oRaBZ6moWeZqGnWehpFnqahZ5mYbPZbP4CmCRMM6i8GFIAAAAASUVORK5CYII="
    return msg



domain = "reddit.com"
msg = receiver()  #base64 data
print(msg)

output_path = "output_image.jpg"  #output path and image format

decode_image(msg, output_path)

 