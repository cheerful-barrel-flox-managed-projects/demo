
from __future__ import print_function

import sys, os, json
from datetime import datetime

def get_runtime_info():
    ret = {}

    # We lose argv0 when going through tyhe nix wrapper currently.
    #ret["argv0"] = sys.argv[0]
    #ret["argv0_abs"] = os.path.abspath(ret["argv0"])
    ret["argv0"] = os.environ.get('NIX_ORIG_ARGV0')
    ret["argv0_abs"] = os.path.abspath(os.environ.get('NIX_ORIG_ARGV0'))
    ret["exec"] = os.path.realpath(sys.argv[0])

    ret["isnix"] = ret["exec"].startswith("/nix/store/")

    if ret["isnix"]:
        elts = ret["exec"].split("/")
        ret["nixpkg"] = elts[3]

        nixshaw_json = "/nix/store/" + ret["nixpkg"] + "/.nixshaw.json"
        if os.path.exists(nixshaw_json):
            data = json.load(open(nixshaw_json))
            for k in ["rev", "date"]:
                if k in data:
                    ret["git"+k] = data[k]
            if "url" in data:
                giturl = data["url"]
                giturl = giturl.replace("https://github.deshaw.com/", "github:")
                ret["giturl"] = giturl
            if "version" in data:
                ret["version"] = data["version"]

    with open("/home/ec2-user/resource-domain.txt") as f:
         ret["resource-domain"] = f.readline().strip()

    if ret["argv0"] == ret["argv0"]:
        del ret["argv0_abs"]

    ret["time"] = datetime.now().strftime("%H:%M:%S")

    return ret

