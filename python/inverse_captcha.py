#!/usr/bin/env python3


TEXT = """87893823215734275675425471658697512539486529734
932123658657466299442989425982853684278119925216918274344
943523119443636821859946339154446174547292291656241485427
544998344282834446389361828242524264332282291685793524214
163618785991962688579157226827244271198836776286574134146
727471814925517368683926587418417698556199645425316578419
292945367832693772857178121215534659243287424474181616632
869395852993836757566966322833556643527348433145288317598
195567933532723199545223111893639319258333822259598252283
346853326222487463744962464431841874861794941793922898829
339194145772264193641745624389418266819717425578644599456
747758271569233624924325471165352987133612982573524966742
523857395233992294821421887241785852519964219458844854356
547484727298423263746666469521717635828378878184317163684
121567585177898461937757569644736684485428953421528695972
768841973197663132383389224743814982997585616175512285764
373194591333555628881711299391169497266765691423899929183
199716341254897764949122721947779612413495852784321382479
268511769663151214124149645184575865527618659772474843299
627649852791129253118529214994813972434584158478235221492
163485873467111849542414343728297924334783125828585125957
913343318238744465638667983158493339791513278541168668844
773169677645962192482166711275178988498788399184581851324
999476754352616946376697579146475652691158739976473655795
946492335389692134294482183399145712525632956448963135226
872245762851456412823148738211168297688683819241299693292
437333752426213539925665863841851523987673286659673188877
953257324371312823841923496319558998753946722151753527238
489952438626726895948488137994479639225541983874316471427
546345935174129658646521368985374385651858345184966159284
487926419676186748125877839362358488453524623979417898138
763231123811536217857689912142542811469615865297627739222
422626824233258954675747768339826429492944259213194939826
188454842795147212884132837681924195515342345253153841349
257726234836958139992564762462386829946843685966715246397
494943635958993113623624792955489967913974616255418385527
871357424421185422782996944315147898641333342914479666442
375481825617286281287768867551414226523999252977626284432
9188218189254491238956497568"""

def main():
    """Megallapitja azon szamjegyek osszeget, amelyek azonosak a ráakovetkezo szamjeggyel."""
    lst0 = list(TEXT.splitlines())
    lst = ''.join(lst0)
    num_lst = [int(x) for x, y in zip(lst[::1], lst[1::1]) if int(x) == int(y)]
    if lst[0] == lst[-1]:
        num_lst.append(int(lst[0]))
    total = sum(num_lst)
    print(total)

########################

if __name__ == "__main__":
    main()