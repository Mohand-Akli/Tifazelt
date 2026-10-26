import os,re,sys,json,collections,unicodedata
root=sys.argv[1]
N=lambda s: unicodedata.normalize('NFC',s)
files=[]
for dp,dn,fn in os.walk(root):
    dn[:]=[d for d in dn if not d.startswith('.')]
    for f in fn:
        if f.startswith('.'): continue
        files.append(os.path.relpath(os.path.join(dp,f),root))
md=[f for f in files if f.endswith('.md')]
byname=collections.defaultdict(list)
for f in files:
    b=N(os.path.basename(f)); byname[b[:-3] if b.endswith('.md') else b].append(f); byname[b].append(f)
heads={}
alias={}
for f in md:
    t=open(os.path.join(root,f),encoding='utf-8',errors='replace').read()
    hs=set()
    for m in re.finditer(r'^#{1,6}\s+(.*?)\s*$',t,re.M):
        h=re.sub(r'[\*\_`]','',m.group(1)).strip(); hs.add(N(h).lower())
    heads[f]=hs
    fm=re.match(r'^---\n(.*?)\n---',t,re.S)
    if fm:
        for a in re.findall(r'^\s*-\s*(.+)$',fm.group(1).split('aliases:')[-1],re.M) if 'aliases:' in fm.group(1) else []:
            alias[N(a.strip().strip('"\''))]=f
link=re.compile(r'(!?)\[\[([^\]\|#]*)(#[^\]\|]*)?(\|[^\]]*)?\]\]')
broken=collections.Counter(); brokenh=collections.Counter(); inlinks=collections.Counter(); where=collections.defaultdict(set)
conflicts=[]; empty=[]
for f in md:
    t=open(os.path.join(root,f),encoding='utf-8',errors='replace').read()
    if re.search(r'^(<<<<<<<|>>>>>>>|=======$)',t,re.M): conflicts.append(f)
    if len(t.strip())==0: empty.append(f)
    for m in link.finditer(t):
        tgt=N(m.group(2).strip()); h=m.group(3)
        if tgt=='' : tf=f
        else:
            base=os.path.basename(tgt)
            c=byname.get(base) or byname.get(base+'.md') or ([alias[tgt]] if tgt in alias else None)
            if not c: broken[tgt]+=1; where[tgt].add(f); continue
            tf=c[0]
        inlinks[tf]+=1
        if h and tf.endswith('.md'):
            hh=N(re.sub(r'[\*\_`]','',h[1:])).strip().lower().rstrip("\\").strip()
            if hh.startswith('^'): continue
            if hh not in heads.get(tf,set()): brokenh[(tf,h[1:])]+=1; where[('H',tf,h[1:])].add(f)
dups={k:v for k,v in byname.items() if len(set(v))>1 and not k.endswith('.md')}
mode=sys.argv[2] if len(sys.argv)>2 else 'summary'
gdd=[f for f in md if not f.startswith('CSV import')]
print('notes md',len(md),'hors CSV',len(gdd))
print('conflits',conflicts); print('vides',empty)
print('doublons de nom',{k:v for k,v in dups.items()})
print('liens cassés',sum(broken.values()),'cibles',len(broken))
for k,v in broken.most_common(200): print('  ',v,k,'<-',sorted(where[k])[:4])
print('ancres cassées',sum(brokenh.values()))
for (tf,h),v in brokenh.most_common(200): print('  ',v,tf.split('/')[-1],'#',h,'<-',sorted(where[('H',tf,h)])[:3])
orph=[f for f in gdd if inlinks[f]==0]
print('orphelins hors CSV',orph)
csvorph=sum(1 for f in md if f.startswith('CSV import') and inlinks[f]==0)
print('CSV import sans lien entrant',csvorph)
