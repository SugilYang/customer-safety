# 한 번에: 자료 생성 → ETS판 → 협력사판 → 저장소 루트로 복사
import os, json, shutil, subprocess, sys
here=os.path.dirname(os.path.abspath(__file__)); root=os.path.dirname(here)
os.makedirs(os.path.join(here,'out','partners'),exist_ok=True)
run=lambda f: subprocess.run([sys.executable, os.path.join(here,f)], check=True, cwd=here)
run('build_data.py')
d=json.load(open(os.path.join(here,'data.json'),encoding='utf-8'))
open(os.path.join(root,'data.js'),'w',encoding='utf-8').write('window.FALLBACK_DATA='+json.dumps(d,ensure_ascii=False)+';')
run('build_app.py'); run('build_partner.py')
shutil.copy(os.path.join(here,'out','index.html'), os.path.join(root,'index.html'))
shutil.copy(os.path.join(here,'out','partners','index.html'), os.path.join(root,'partners','index.html'))
print('완료:', d['version'])
