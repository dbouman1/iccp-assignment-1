{"filter":false,"title":"main.py","tooltip":"/main.py","undoManager":{"mark":2,"position":2,"stack":[[{"group":"doc","deltas":[{"start":{"row":24,"column":33},"end":{"row":24,"column":35},"action":"remove","lines":[",1"]},{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"insert","lines":["    total_energy[t] = np.add(kin_energy[t],pot_energy[t])",""]},{"start":{"row":50,"column":22},"end":{"row":50,"column":23},"action":"insert","lines":["="]},{"start":{"row":52,"column":0},"end":{"row":52,"column":5},"action":"remove","lines":["    \t"]},{"start":{"row":71,"column":8},"end":{"row":71,"column":11},"action":"remove","lines":["val"]},{"start":{"row":71,"column":8},"end":{"row":71,"column":13},"action":"insert","lines":["energ"]},{"start":{"row":72,"column":8},"end":{"row":72,"column":11},"action":"remove","lines":["val"]},{"start":{"row":72,"column":8},"end":{"row":72,"column":13},"action":"insert","lines":["energ"]},{"start":{"row":72,"column":20},"end":{"row":73,"column":21},"action":"remove","lines":["val.translate(None, '[]').replace(\" \", \"\")","    with open(\"output"]},{"start":{"row":72,"column":20},"end":{"row":83,"column":25},"action":"insert","lines":["energ.translate(None, '[]').replace(\" \", \"\")","    with open(\"total_energy.dat\", \"a\") as f_energ:","        f_energ.write(out_energ)","        ","    out_kin = str(kin_energy[t]) + \"\\n\"","    out_kin = out_kin.translate(None, '[]').replace(\" \", \"\")","    with open(\"kin_energy.dat\", \"a\") as f_kin:","        f_kin.write(out_kin)","        ","    out_pot = str(pot_energy[t]) + \"\\n\"","    out_pot = out_pot.translate(None, '[]').replace(\" \", \"\")","    with open(\"pot_energy"]},{"start":{"row":83,"column":41},"end":{"row":83,"column":42},"action":"remove","lines":["h"]},{"start":{"row":83,"column":41},"end":{"row":83,"column":45},"action":"insert","lines":["_pot"]},{"start":{"row":84,"column":9},"end":{"row":84,"column":10},"action":"remove","lines":["h"]},{"start":{"row":84,"column":9},"end":{"row":84,"column":13},"action":"insert","lines":["_pot"]},{"start":{"row":84,"column":24},"end":{"row":84,"column":27},"action":"remove","lines":["val"]},{"start":{"row":84,"column":24},"end":{"row":84,"column":27},"action":"insert","lines":["pot"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["w"]}]}]]},"ace":{"folds":[],"scrolltop":386.5,"scrollleft":0,"selection":{"start":{"row":37,"column":30},"end":{"row":37,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":24,"state":"start","mode":"ace/mode/python"}},"timestamp":1424762921500,"hash":"b9db3a897375ad83a1a40f87995261c6d1deb0b8"}