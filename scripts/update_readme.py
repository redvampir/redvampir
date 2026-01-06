content = '''<div align="center">

![header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Привет,%20я%20Павел!&fontSize=42&fontColor=fff&animation=fadeIn&fontAlignY=35&desc=Web-разработчик%20|%20VS%20Code%20Plugins%20|%20Neural%20Networks&descSize=16&descAlignY=55)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=A855F7&center=true&vCenter=true&random=false&width=600&lines=Junior+Web+Developer;VS+Code+Plugin+Creator;Neural+Network+Explorer;Always+Learning+New+Things)](https://git.io/typing-svg)

---

### 🚀 Обо мне

🌐 Web-разработчик на старте карьеры  
🧩 Создаю плагины для VS Code  
🤖 Разрабатываю свою нейросеть  
📚 Постоянно учусь и экспериментирую

---

### 🛠 Технологии

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white)

---

### 📊 GitHub Статистика

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=redvampir&show_icons=true&theme=radical&hide_border=true&count_private=true"/>
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=redvampir&layout=compact&theme=radical&hide_border=true"/>

---

### 📫 Связаться со мной

[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/PavelKrovorov)

---

![footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer)

</div>
'''

with open('README.md','w',encoding='utf-8') as f:
    f.write(content)

import subprocess
subprocess.run(['git','add','README.md'])
subprocess.run(['git','commit','-m','fix: renderable README (remove CDATA/code fence)'])
subprocess.run(['git','push','-u','origin','main'])
