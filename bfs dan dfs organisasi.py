organisasi =  {'rektor':set(['pembina']),
         'pembina':set(['rektor','ketua']),
         'ketua':set(['pembina','wakil','sekretaris','bendahara']),
         'sekretaris':set(['ketua','wakil','bendahara']),
         'bendahara':set(['ketua','wakil','sekretaris']),
         'wakil':set(['ketua,sekretaris','bendahara','humas','kepala divisi','perkap','litbang','sdm']),
         'humas':set(['wakil','humas ekstern','humas intern','kepala divisi','perkap','litbang','sdm']),
         'kepala divisi':set(['wakil','divisi gh','divisi rc','divisi rc','divisi cv','humas','perkap','litbang','sdm']),
         'perkap':set(['wakil','peralatan','perlengkapan','kepala divisi','humas','litbang','sdm']),
         'litbang':set(['wakil','penelitian','pengembangan','kepala divisi','perkap','humas','sdm']),
         'sdm':set(['wakil','pengolahan atlit','official atlit','kepala divisi','perkap','litbang','humas']),
         'humas intern':set(['humas','humas ekstern']),
         'humas ekstern':set(['humas','humas intern']),
         'perlengkapan':set(['perkap','peralatan']),
         'peralatan':set(['perkap','perlengkapan']),
         'divisi gh':set(['kepala divisi','divisi rc','4','divisi cv']),
         'divisi rc':set(['kepala divisi','divisi gh','4','divisi cv']),
         'divisi cv':set(['kepala divisi','divisi rc','4','divisi gh']),
         'penelitian':set(['litbang','pengembangan']),
         'pengembangan':set(['litbang','penelitian']),
         'pengolahan atlit':set(['sdm','official atlit']),
         'official atlit':set(['sdm','pengolahan atlit']),
         
         }
def bfs(graf,mulai,tujuan):
    
    queue = [[mulai]]
    visited = set()

    while queue:     
       
        jalur = queue.pop(0)

        
        state = jalur[-1]
        if state == tujuan:        
            return jalur       
        elif state not in visited:
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                queue.append(jalur_baru) 

           
            visited.add(state)

        
        isi = len(queue)
        if isi == 0:
            print("Tidak ditemukan")

def dfs(graf, mulai, tujuan):
    stack = [[mulai]]
    visited = set()

    while stack:
        
        panjang_tumpukan = len(stack)-1
        
       
        jalur = stack.pop(panjang_tumpukan)

        
        state = jalur[-1]

        
        if state == tujuan:
            return jalur
        
        elif state not in visited:
            
            for cabang in graf.get(state, []): 
                jalur_baru = list(jalur) 
                jalur_baru.append(cabang) 
                stack.append(jalur_baru)

            
            visited.add(state)


        
        isi = len(stack)
        if isi == 0:
            print("Tidak ditemukan")
