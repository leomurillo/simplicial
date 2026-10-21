"""Grow the verified basin by increasing the ceiling, not by assuming termination."""
from pathlib import Path
import json
from peak_bottleneck_audit import predecessors


def main():
    limit=1_000_000
    inside=bytearray(limit+1)
    inside[1]=1
    size=1;gap=2
    gap_events=[];mass_records=[];largest_mass=0;largest_stall=None
    snapshots=[]
    targets={16,160,9231,9232,13120,250504,500000,1000000}
    for H in range(2,limit+1):
        added=[];previous_gap=gap
        if H%2==0 and inside[H//2]:
            stack=[H]
            while stack:
                x=stack.pop()
                if inside[x]:continue
                inside[x]=1;added.append(x)
                if 2*x<=H and not inside[2*x]:stack.append(2*x)
                if x%6==4:
                    y=(x-1)//3
                    if y>1 and not inside[y]:stack.append(y)
            size+=len(added)
            while gap<=H and inside[gap]:gap+=1
        if H>4 and len(added)>1:assert H%12==4
        if gap!=previous_gap:
            gap_events.append(dict(H=H,old_gap=previous_gap,new_gap=gap,added=len(added),basin_size=size))
        if len(added)>largest_mass:
            largest_mass=len(added)
            mass_records.append(dict(H=H,added=largest_mass,gap=gap,gap_advanced=gap!=previous_gap))
        if added and gap==previous_gap and (largest_stall is None or len(added)>largest_stall['added']):
            largest_stall=dict(H=H,added=len(added),gap=gap,basin_size=size)
        if H in targets:
            direct=predecessors(1,H)
            assert len(direct)==size
            assert all(inside[x] for x in direct)
            assert gap==next(x for x in range(2,H+2) if x not in direct)
            snapshots.append(dict(H=H,basin_size=size,first_missing=gap,covered_initial_interval=gap-1))
    result=dict(status='passed',limit=limit,method='height activation and bounded inverse propagation',
                snapshots=snapshots,gap_events=gap_events,mass_records=mass_records,
                largest_jump_without_gap_progress=largest_stall)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
