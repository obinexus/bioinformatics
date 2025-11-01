
--------------------------------------------------
Quick smoke test
--------------------------------------------------
1. Create a toy partial graph (JSON):

```
echo '{"0":[1,2],"1":[0,3],"2":[0,3],"3":[1,2,4],"4":[3]}' > partial.json
```

2. Create a 128-byte Bloom filter that *accepts* every edge in that graph:

```
python3 -c "
import hashlib, struct
bf = bytearray(128)
def setbit(b, idx): b[idx//8] |= 1<<(idx%8)
def h(x,i): return int.from_bytes(hashlib.sha256(f'{x}:{i}'.encode()).digest()[:4],'little') % (128*8)
edges = [(0,1),(0,2),(1,3),(2,3),(3,4)]
for a,b in edges:
    for i in range(3): setbit(bf, h((a,b),i))
open('hints.bin','wb').write(bf)"
```

3. Run:

```
chmod +x sparse_exit.py
./sparse_exit.py hints.bin partial.json
```

Typical output (one possible Hamiltonian path):

```
0 2 3 1 0
```

