target = "xilinx"
action = "synthesis"

fetchto = "../../ip_cores"

syn_device = "xc6slx45t"
syn_grade = "-3"
syn_package = "fgg484"
syn_top = "spec_top"
syn_project = "finedelay_spec_1_1.xise"

modules = { "local" : [ "../../top/spec_1_1" ] }
