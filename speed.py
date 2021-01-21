import speedtest
st= speedtest.Speedtest()

print("Download Speed: {:5.2f} MB/s".format(st.download()/(8e+6)))
print("Upload Speed: {:5.2f} MB/s".format(st.upload()/(8e+6)))
