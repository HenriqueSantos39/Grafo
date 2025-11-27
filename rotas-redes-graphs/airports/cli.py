# airports/cli.py
import argparse
from airports.graph import DirectedWeightedGraph

def main():
    p = argparse.ArgumentParser(prog='airports-cli')
    p.add_argument('--list', help='List outgoing flights from airport', metavar='CODE')
    p.add_argument('--add-route', nargs=4, metavar=('SRC','DST','TIME','COST'),
                   help='Add route: SRC DST TIME_MIN COST')
    args = p.parse_args()
    g = DirectedWeightedGraph()
    g.add_route('GRU','GIG', 70, 50.0, 'AZ100')
    g.add_route('GRU','BSB', 100, 80.0, 'AZ200')
    g.add_route('BSB','GIG', 60, 60.0, 'AZ300')
    if args.list:
        out = g.outgoing(args.list)
        for dst, t, cost, fid in out:
            print(f"{args.list} -> {dst}: {t}min, ${cost}, id={fid}")
    if args.add_route:
        src,dst,time,cost = args.add_route
        g.add_route(src,dst,int(time),float(cost))
        print('Route added (in-memory):', src, dst, time, cost)

if __name__ == '__main__':
    main()
