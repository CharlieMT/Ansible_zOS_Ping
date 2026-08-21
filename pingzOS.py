---
- name: "Ping"
  hosts: "{{ host | d('all') }}"
  collections:
    - ibm.ibm_zos_core
​
  environment: 
    ZOAU_HOME: "{{ ZOAU_PATH }}"
    LIBPATH: "/lib:/usr/lib{{ ZOAU_PATH }}"/lib{{ PAYTHON_PATH }}/lib:."
    PATH: "/bin:/var/bin:{{ ZOAU_PATH }}"/bin:{{ PYTHON_PATH }}/bin"
    _CEE_RUNOPTS: "FILETAG(AUTOCVT,AUTOTAG) POSIX(ON)"
    _TAG_REDIR_ERR: "txt"
    _TAG_REDIR_IN: "txt"
    _TAG_REDIR_OUT: "txt"
    _BPXK_AUTOCVT: "ON"
    LANG: "C"
#    PYTHONSTDINENCODING: "cp1047"
#    PYTHONPATH: "/usr/lpp/IBM/cyp/pyz"
  tasks:
  - name: Ping host - {{ host }}
    ping:
    register: result
  - name: Response
    debug:
      msg: "{{ result.ping }}"