import base64, codecs
magic = 'IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgLSotIGNvZGluZzogVVRGLTggLSotCmZyb20gdXJsbGliMiBpbXBvcnQgUmVxdWVzdCwgdXJsb3BlbiwgVVJMRXJyb3IsIEhUVFBFcnJvcgppbXBvcnQgb3MKCmZyb20gdHFkbSBpbXBvcnQgdHJhbmdlCmZyb20gY29sb3JhbWEgaW1wb3J0IEZvcmUKCiMgTG9hZGluZzoKY29sb3JfYmFycyA9WwogICAgRm9yZS5HUkVFTiwKICAgIF0KZm9yIGNvbG9yIGluIGNvbG9yX2JhcnM6CiAgICBmb3IgaSBpbiB0cmFuZ2UoaW50KDcqKjcuNSksICAjNGU1CiAgICAgICAgICAgICAgICAgICAgYmFyX2Zvcm1hdD0ie2xfYmFyfSVze2Jhcn0lc3tyX2Jhcn0iICUgKGNvbG9yLCBGb3JlLlJFU0VUKSk6CiAgICAgICAgcGFzcwoKZGVmIFNwYWNlKGopOgoJaSA9IDAKCXdoaWxlIGk8PWo6CgkJcHJpbnQgIiAiLAoJCWkrPTEKCiNIZWFkaW5nCgpvcy5zeXN0ZW0oJ2NsZWFyJykKcHJpbnQg'
love = 'XPpaWjcpZQZmJmxloDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVNbtVPNtVPO7KlNtVPNtVPNtVPNtVUgsKlNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtr19sK19sK18tVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUgsKjbtVPNtVUgsVS9sVPNtVPNtVPNtVUgsKlNtVPNtVPNtVPNtVPNtr18tVPNtVPNtVPNtr19sVPNtVUgsKlNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUgsKjbtVPNtr18tVUgsKlNtVPNtVPNtVUgsK3gsK18tr19sVUgsKlNtVPO7K18tr19sVPNtr19sVPNtVUgsKlNtVUgsKlNtVPO7K18tr19sVPNtVPO7K18tVPNtVUgsKjbtVPO7K18tVPO7K18tVPNtr19sVUgsKlO7K18tVUgsVPO7K197K18tr19sVPO7K18tr19sK19sK18tVPO7K18tVUgsKlNtr19sVPO7K18tr18tVPO7K18tVUgsKjbtVUgsK19sK18tr19sVPO7KlNt'
god = 'IHtfXyB7X18gIHtfICB7X197X18ge19fICB7X18ge19fICAgICAgIHtfXyAgIHtfXyAge19fICB7X197X19fX18ge19fIHtfXwoge19fICAgICAgIHtfXyB7XyAgIHtfXyB7X18gIHtfICB7X197X18ge19fICB7X18ge19fICAgICAgIHtfXyAgIHtfXyAge19fICB7X197XyAgICAgICAgIHtfXwp7X18gICAgICAgICB7X18ge19fIHtfX3tfX18gIHtfICB7X197X197X19fICB7X18ge19fICAgICAgICAge19fIHtfX197X19fICB7X18gIHtfX19fICAge19fXwoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKCiAgICAgICAgICAgICAgICAgICAgICAgwqljb3B5cmlnaHQgYnkgXDAzM1s5M21FbmdpbmUgUmlwcGVyIFwwMzNbOTdtCgonJycpCnByaW50KCIgIikKCgpkZWYgRmluZGluZ0NvbnRyb2xQYW5lbCgpOgoJZiA9IG9wZW4oIkFkbWluaXN0cmF0b3IudHh0'
destiny = 'VvjvpvVcBjbWoTyhnlN9VUWuq19coaO1qPtvKQNmZ1f5Zz1SoaEypvOGnKEyVR5uoJHtKT4bMKttBvOyrTSgpTkyYzAioFOipvO3q3phMKuuoKOfMF5wo20tXGbtVvxXPKOlnJ50VPWpoykhKQNmZ1f5ZJ1Qo250pz9fVSOuozIfVRMcozEcozptBvOpovVXPKqbnJkyVSElqJH6PtxWp3IvK2kcozftCFOzYaWyLJEfnJ5yXPxXPDycMvOho3Dtp3IvK2kcozf6PtxWPJWlMJSePtxWpzIkK2kcozftCFNvnUE0pQbiYlVeoTyhnlfvYlVep3IvK2kcozfXPDylMKRtCFOFMKS1MKA0XUWypI9fnJ5eXDbWPKElrGbXPDxWpzImpT9hp2HtCFO1pzkipTIhXUWypFxXPDyyrTAypUDtFSEHHRIlpz9lVTSmVTH6PtxWPJAioaEcoaIyPtxWMKuwMKO0VSIFGRIlpz9lVTSmVTH6PtxWPJAioaEcoaIyPtxWMJkmMGbXPDxWpUWcoaDtVxMiqJ5x8W+Hxm0+VPVfpzIkK2kcozfXPDxWPtxWPDbWPDxXPxMcozEcozqQo250pz9fHTShMJjbXD=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
