U
    ��F_`l  �                	   @   s:  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlm	Z
 d dlZd dlZd dlZd dlm	Z	 d dlmZ d dlZe�d d�Ze�d� dd� Zdd	� Zd
d� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� ZdddgZdZeee � ee� ed �Z e d!k�rBed"�Z!eed#e! �� �qe d$k�rVe�  �qe d%k�rje�  �qe d&k�r~e�  �qe d'k�r�e�  �qe d(k�r�e�  �qe d)k�r�e�  �qe d*k�r�e�  �qe d+k�r�e�  �qe d,k�r�e�  �qe d-k�red.�Z"e�d/e" � �qe d0k�rnd Z#d1Z$e�%d2� �ze&d3d4�Z'e'�(� Z$e$d1k�r\d1Z$n�e&d3d4��Z)e)�(� �*� Z+W 5 Q R X e,e-e+��D ]Z.ed5e+e.  d6 � �q�e+d2 Z/e/dd7� Z0e0d8d� Z0e&d9d4��Z)e)�(� �*� Z1W 5 Q R X e,e-e1��D ](Z2e0e1e2 k�r�ed5e1e2  d6 � �q�e&d3d:�Z3e3�4d1� e3�5�  W n(   e&d3d;�Z6e6�4d1� e6�5�  Y nX �q,�qe d<k�r�ed.�Z"e�d=e" � �qe dk�s�e d>k�s�e d?k�r�e dk�r�e�d� ee� �qe d@k�r"d Z#d1Z$e�%d2� �ze&dAd4�Z'e'�(� Z$e$d1k�rd1Z$n�e&dBd4��Z)e)�(� �*� Z+W 5 Q R X e,e-e+��D ]Z.ed5e+e.  d6 � �q@e+d2 Z/e/dd7� Z0e0d8d� Z0e&d9d4��Z)e)�(� �*� Z1W 5 Q R X e,e-e1��D ](Z2e0e1e2 k�r�ed5e1e2  d6 � �q�e&dAd:�Z3e3�4d1� e3�5�  W n(   e&dAd;�Z6e6�4d1� e6�5�  Y nX �q�nedCe  dD � �qdS )E�    N)�BeautifulSoup)�VkUpload�   �clearc               )   C   s2  t d�} dddddddd	d
dddddddddddddddddddddd d!d"d#d$d%d&d'd(d)d*g)}d+}td,� z�|d-kr�t�d.|  d/ ||  �}nt�|| d0 |  �}|r�|d-kr�td1|  d/ ||  d2 � q�td3||  d0 |  d2 � ntd4� W n   td4� Y nX |d5 t|�k�r$�q.|d57 }qjd S )6Nu(   [35m|  |-[Укажите ник]->[0m zhttps://vk.com/zhttps://my.mail.ru/mail/zhttps://www.drive2.ru/users/zhttps://twitter.com/zhttps://github.com/zhttps://instagram.com/z+http://forum.3dnews.ru/member.php?username=zHhttps://4pda.ru/forum/index.php?act=search&source=pst&noform=1&username=z https://forums.adobe.com/people/zhttps://ask.fm/zhttps://badoo.com/profile/zhttps://www.bandcamp.com/z!https://bitcoinforum.com/profile/zblogspot.comzhttps://dev.to/zhttps://www.ebay.com/usr/z!https://www.gamespot.com/profile/zhttps://ok.ru/z0https://play.google.com/store/apps/developer?id=z"https://pokemonshowdown.com/users/zhttps://www.reddit.com/user/zhttps://steamcommunity.com/id/z"https://steamcommunity.com/groups/zhttps://tamtam.chat/zhttps://t.me/zhttps://www.tiktok.com/@zhttps://www.twitch.tv/z,https://data.typeracer.com/pit/profile?user=z$https://www.wikipedia.org/wiki/User:z#https://yandex.ru/collections/user/zhttps://www.youtube.com/zhttps://www.baby.ru/u/z"https://www.babyblog.ru/user/info/z&https://www.geocaching.com/profile/?u=zhttps://habr.com/ru/users/zhttps://pikabu.ru/@zhttps://spletnik.ru/user/zhttps://www.facebook.com/zhhttps://zen.yandex.ru/z'https://ggscore.com/ru/dota-2/player?t=z https://www.facebook.com/public/r   z[35m|   |_[0m�   zhttps://�.� z[35m|     |- https://�[0mz[35m|     |- u.   [33m|     |-[Нет результата][0m�   )�input�print�requests�get�len)ZnickZ	urls_siteZset_iZscan_s� r   �sherl.py�nick_search	   sv    �) r   c                  C   sX  t d�} z�t�d| � ���� }tdt|d � d t|d � d t|d � d	 t|d
 � d t|d � d t|d � d t|d � d t|d � d t|d � d t|d � d t|d � d t|d d � � W n   td� Y nX | }z�dddd d!�}tjd"| |d#�}t|jd$�}|jd%d&��d'�}|�	d(�}|D ]�}|j	d)d&�\}	}
|	j
|
j
 }	}
|jd*d&�j
}|jd+d&�j
�d,d-��d.d-�}|jd/d&�j
}td0|	� d1|
� d2|� d3|� d4|� d5�� �qPW n   td6� Y nX |d d7� }td8d9��}|�� �� }W 5 Q R X tt|��D ](}||| k�r*td:||  d; � �q*d S )<Nu$   [35m|  |-[Укажите IP]-> [0mzhttp://ip-api.com/json/z[36m|     |-[Country]: [32mZcountryz"
[36m|     |-[CountryCode]: [32mZcountryCodez
[36m|     |-[Region]: [32mZregionz"
[36m|     |-[Region Name]: [32mZ
regionNamez
[36m|     |-[City]: [32mZcityz
[36m|     |-[Zip]: [32m�zipz
[36m|     |-[Latinude]: [32mZlatz 
[36m|     |-[Longitude]: [32mZlonz
[36m|     |-[Timezone]:[32m �timezonez
[36m|     |-[ISP]:[32m Zispz
[36m|     |-[Org]:[32m Zorgz
[36m|     |-[As]:[32m �asz
[36m|[0mu1   [31m|  |-Неизвестная ошибка[0mzgMozilla/5.0 (Windows NT 10.0; ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36�
keep-aliveziknowwhatyoudownload.comz https://iknowwhatyoudownload.com)�
User-Agent�
Connection�HostZRefererz-https://iknowwhatyoudownload.com/ru/peer/?ip=��headers�html.parser�table�Zclass_ZtbodyZtrzdate-columnzcategory-columnzname-column�
r   z    zsize-columnuB   [36m|     |-[Использовано первый раз]: [32muI   
[36m|     |-[использовано последний раз]: [32mu,   
[36m|     |-[тип торента]: [32mu6   
[36m|     |-[название торента]:[32m u2   
[36m|     |-[размер торента]: [32mz
[36m|[32m[0mu5   [31m|     |-Неизвестная ошибка [0m������bdclean.txt�r�[36m|     |-[32mr	   )r   r   r   �jsonr   �str�BS�content�find�find_all�text�replace�open�read�
splitlines�ranger   )Zqueryr"   �	target_ipr   �page�soupr   ZtorrentsZtorrent�firstZlast�category�name�size�a�f�nums�ir   r   r   �ip_infoH   s8    �
0r;   c               	   C   s�  t d�} z�t�d|  �}tdd�}t|jd�j}|�|� |��  tdd��}|�� �	� }W 5 Q R X t
t|�d �D ]Z}|| dkrt|| d	 d
kr�td� td||  d � td� qttd||  d � qtt�d|  �}|jdkr�d|  }n W n   td� Y nX z~t�d|  �}	t|	jd�}
|
jdd�}|
�d�}|D ]}td|jd� �q@|
jdd�}|
�d�}|D ]}td|jd� �qpW n   td� Y nX | }tdd��}|�� �	� }W 5 Q R X t
t|��D ](}||| k�r�td||  d � �q�d |  }t�|�}t|jd�}
|
jd!d"d�d	 �� �d#d�}tdd�}|�t|�� |��  tdd��}|�� �	� }W 5 Q R X t
t|��D ]p}|| dk�r�|| d	 d
k�r�td� td||  d � td� n$td|| �d$d��d#d� d � �q�d S )%Nu-   [35m|  |-[Укажите номер]-> [0m+z2https://htmlweb.ru/geo/api.php?short=link&telcod=+�SPN.txt�wZlxmlr"   r
   r   r   �+�   [36m|  |‾[0m�[36m|  |-[�] [0m�[36m|  |_[0m�[36m|     |-[z$https://api.whatsapp.com/send?phone=��   u5   [31m|     |-Неизвестная ошибка[0m z/https://mirror.bullshit.agency/search_by_phone/r   zmedia-headingr   Zh4u   [36m|     |-[Имя]: [32mr	   z
text-muted�spanu8   [36m|     |-[Адрес и информация]: [32m�4   [31m|     |-Неизвестная ошибка[0mr!   r#   z!https://phonebook.space/?number=+�div�results�  �,)r   r   r   r,   r   r*   �write�closer-   r.   r/   r   r   Zstatus_coder&   r(   r)   �get_textr+   r%   )Zphone�response�fileZ	cleantextr8   �spn_textZoooseZutyZutl2r1   r2   Z	classsellZnamesellZ	classtextZnametextr7   r9   r:   �url�s�ttxZoooer   r   r   �
phone_infof   sr    









rT   c                 C   s   t �| �jS )N)r   r   r*   )rQ   r   r   r   �get_html�   s    rU   c              	   C   s�   d}t | d�}|�d�D ]}||�� 7 }qtdd�}|�|� |��  tdd��}|�� �� }W 5 Q R X tt	|��D ]j}|| dkrt|| d dkr�t
d	� t
d
||  d � t
d� qtt
d|| �dd��dd� d � qtd S )Nr   r   Ztdr<   r=   r"   r   r>   r?   r@   rA   rB   rC   rI   rJ   z,
|     |-|||)r&   ZfindAllZgetTextr,   rK   rL   r-   r.   r/   r   r   r+   )ZautoserZdat_autor2   �xrO   r8   rP   Zooqoer   r   r   �auto_ua�   s     



rW   c                  C   s  t d�} t d�}t�d|  d | d �}|�� }z�tt|d d ��D ]�}td� td	t|� d
 t|d d | d � d t|d d | d � d � td� z(tdt|d d | d � d � W qH   Y qHX qHtd|d� W n    td� td|d� Y nX d S )Nu@   [35m|  |-[Укажите ID юзера]-> [0mhttps://vk.com/idu-   [35m|  |-[Укажите токен]->[30m z8https://api.vk.com/method/newsfeed.getMentions?owner_id=z&count=50&access_token=�&v=5.50rN   �itemsz---------------------------z[36m|  |-[[33mz[36m][32m https://vk.com/wallZto_id�_�idr	   z[36m|  |[0mu   [36m|  |-[Текст]: [32mr*   u&   [36m|
|==|-[Результат]:[32mrF   u"   [31m|     |-Информация:)r   r   r   r$   r/   r   r   r%   )�iduser�tokenr"   ZdatarZpcr   r   r   �	ya_search�   s"    L(r^   c                  C   s�  t d�} t d�}d}d}d}d}d}d}td� t�d� t�d|  d | d �}|�� }	t|	d	 d
 �}
|dkr�|
dkr�td� t�|	d	 d �}t|j	�d }d}n"|
dkr�td� d}ntd� d}q0|dkr�|
dkr�d}q0|dkr�|
dkr�d}q0|dkr0t�|	d	 d �}|dkr0|t|j	�d k�r2q0||k�rL|dk�rLd}q0|t|j	�d kr0|t|j	�d kr0|dkr0tdt|j
� d t|j	� d � d}t|j	�d }|}q0d S )Nu@   [35m|  |-[Укажите ID юзера]->[0m https://vk.com/idu,   [35m|  |-[Укажите токен]-> [0mr   z[36m|    |_[0m�   z;https://api.vk.com/method/messages.getLastActivity?user_id=z&access_token=rX   rN   Zonline�1u+   [36m|     |-[Status]: [32mВ сети[0m�timer
   �0u7   [36m|     |-[Status]:[31mВышел из сети[0mr   u4   [36m|     |-[Status]:[33m Неизвестно[0m�   z[36m|     |-[[34m�:u}   [36m]:[33m Есть актив. Возможно юзер отправил сообщение или открыл вк;[0m)r   r   ra   �sleepr   r   r$   r%   �	localtime�tm_sec�tm_min)r\   r]   Znew_timeZold_timeZcheckZ
check_timeZonline_offlineZold_and_new_timer"   Z	onliflineZ	online_ynZresult_timer   r   r   �vk_track�   sP    
,$ri   c               
   C   s�  d} t d� td�}td�}td�}td�}t�d| �}dd	� }d
g}d}tt|��D ]}	|||	 |�dkrX||	 }qX|| kr,�zLtj||dd�}
|
jdd� |
}t	|
�}|j
d| d | |d�d d d d }t�d� t�d| d | � dddddddddd �	}d!| d" }tj||d#�}t�d$� t|jd%�}|jd&d'd(�}d}|d �d)�D ]}|d*|��  7 }�q^t |� t�d+| d, � t�d-� t�d+| d, � t�d-� t�d+| d, � |} W q,   Y q,X q,d S ).Nr   ux   [35m|  |-[Укажите полный путь к фотографиям куда камера сохроняет.][0mu7   [35m|  |-[Укажите полный путь]-> [0mu'   [35m|  |-[ID альбома vk]-> [0mu   [35m|  |-[Логин]-> [0mu   [35m|  |-[Пароль]-> [0mz../c                 S   s$   |D ]}|� � | � � kr dS qdS )NTF)�lower)Zstr_�forma�wordr   r   r   �is_part_in_list  s    z$EyeSherlock.<locals>.is_part_in_listZjpgTZ2685278)ZloginZpasswordZapp_id)Z
token_only�/)ZphotosZalbum_idr   Zsizes�   rQ   ztermux-toast -s "Loading..."zrm ../�	yandex.ru�NMozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0�Jtext/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8�en-US,en;q=0.5�gzip, deflate, brr   �  mm-pp=1; mm-pp=1; cpw=1696; cph=829; ob=; i=amWsLIdsYx+AgqsqZjk0mJU9cm24//YIjzynW6zNIM7cVAHpMFdCCLNdzBD8OWekEC/6a3qQ5vrWJu6N6ng8jMWWye8=; yandexuid=5595171361585316044; yp=1629383220.p_sw.1597847220#1609494103.szm.1_25:1536x864:1536x750#1625327355.ygu.1#1907222827.udn.cDphbnZAMWhva2FnZS5ydQ%3D%3D#1618473426.stltp.serp_bk-map_1_1586937426#1626127366.p_cl.1594591366#1907222827.multib.1#1597949194.nps.6834361510%3Aclose; yabs-frequency=/5/1G0M04etFL_oh3TV/q_ToS9G0002iF26nTh1mbG000AmyO6fsi72L0000h3nWlbcmS9K0002jFA0327ImS000002iF22qLB1m00000AmyuALqi7000000hJoW1V1Di7000000h3oWK72mS000002iF808Lh1m00000Aqy805wIh1m00000Amy80jMi7000000h3p0qd6mS000002jFE04vdAmS000002iF600/; ymex=1900676045.yrts.1585316045; _ym_uid=1585316046820045250; mda=0; cycada=i0RRRJ75jNBQnxAa5EFKdHOF2CQDi+jGi/pkQHpH8XY=; gdpr=0; yandex_gid=33; font_loaded=YSv1; my=YwA=; Session_id=3:1597782150.5.1.1585853105949:su7pXg:7.1|896890286.-1.0.1:192608744|1130000045067155.-1.2.2:6009722|221625.143283.QGAphvBZwjrg8FY3Jgr6feu5EYc; sessionid2=3:1597782150.5.1.1585853105949:su7pXg:7.1|896890286.-1.0.1:192608744|1130000045067155.-1.2.2:6009722|221625.239638.q8lmSejfa4e6CQcKT343-RJhV3Y; L=cilkWXt4Z2FlVkh2XkNXYUZhWXtNBlJbWFgQKWkvHiEsF1dGHRo=.1591862827.14262.342587.3f2d006dc101f2d74521a58f68c9901f; yandex_login=anv@1hokage.ru; _ym_d=1594122280; skid=2244826351597682153; _ym_isad=2; ys=svt.1#wprid.1597862291841866-308855603996625660849862-production-app-host-man-web-yp-334; _ym_visorc_26812653=br`   �Trailers�	r   r   ZAcceptzAccept-LanguagezAccept-Encodingr   ZCookiezUpgrade-Insecure-RequestsZTE�$https://yandex.ru/images/search?url=�&rpt=imageview&from=tabbarr   ztermux-toast -s 100%r   rG   zTags Tags_type_simpler   r7   z | ztermux-toast -s "�"r   )r   r   �os�listdirr/   r   �vk_apiZVkApiZauthr   Zphoto�systemr   r   r   r*   r)   rM   ra   re   )Zlast_pZcamZalbumZlogin1Z	password1�filesrm   rk   ZloadprV   Z
vk_sessionZvksZupload�ph�headrQ   rR   r2   rS   ZptextresZlinkr   r   r   �EyeSherlock�   sb    
*
�


r�   c            	   	   C   s�   t d�} d|  d }t�|�}t|jd�}|jddd�d �� �d	d
�}tdd�}|�	t
|�� |��  tdd��}|�� �� }W 5 Q R X tt|��D ]b}|| d
kr�|| d dkr�td� td||  d � td� q�td|| �dd
� d � q�d S )Nu5   [35m|  |-[Укажите ник или И.Ф]->[0m z https://phonebook.space/?number=z&check=Namer   rG   rH   r   r   rI   r   r<   r=   r"   r>   �   [35m|  |‾[0m�[35m|  |-[rA   �[35m|  |_[0m�[35m|    |-[rJ   )r   r   r   r   r*   r)   rM   r+   r,   rK   r%   rL   r-   r.   r/   r   r   )	ZnornrQ   rR   r2   rS   rO   r8   rP   Zoqooer   r   r   �SPN6  s"    


r�   c               	   C   sX  t d�} td� td� t�d� td� d|  d }t�|�}td� t�d	� t�|�}t|jd
�}|jddd�d �	� }|jddd�d �	� }t
dd�}|�|| � |��  t
dd��}|�� �� }W 5 Q R X d}	tt|��D ]l}
||
 dkr�||
 d dk�r.td� td||
  d � td� q�td||
 �dd��dd� d � q�d S )Nu@   [35m|  [Укажите номер авто](С777СС97)-> [0mu3   [35m|    |-[Загрузка данных...] [0muC   [35m|    |-[Это может занять 1 минуту...] [0mr_   u2   [35m|    |-[Запрос на отчет...] [0mzhttps://autois.ru/num/r   u+   [35m|    |-[Сбор данных...] [0m�7   r   rG   ztable-responsive-lgr   r
   zcard-headerr<   r=   r"   r   r>   r�   r�   rA   r�   r�   rJ   u   В полном отчетеu   Неизвестно)r   r   ra   re   r   r   r   r*   r)   rM   r,   rK   rL   r-   r.   r/   r   r+   )�numrQ   rR   r2   rS   ZautonamerO   r8   rP   ZotwoZoooear   r   r   �auto_ruK  s4    





r�   c               
   C   s   t d� td�} ddddddd	d
dd�	}d|  d }tj||d�}t|jd�}|jddd�}tt|��D ]�}t d|| �	�  d � || jddd�}t�|d d �}t|jd�}	|	jddd�}
t d|
d d �
d d!��
d"d!��
d#d!� d � t d$� qhd S )%NuW   [35mоПддерживает расширения [[32mJPG, ICO, GIF, PNG, JPEG[35m]u;   [35m|  [Укажите ссылку на фото]--> [0mrp   rq   rr   rs   rt   r   ru   r`   rv   rw   rx   ry   r   r   rG   zother-sites__snippetr   z[32m|    |-[TITLE] [34mr	   r7   T)�hrefr   r�   �meta)r'   z[32m|    |-[URL] [33mr
   r'   z0;URL='r   �'rz   z[32m|    |[0m)r   r   r   r   r   r*   r)   r/   r   rM   r+   )r�   r�   rQ   rR   r2   ZsdatasZttoZuurslZurldumpZurlsoup�mer   r   r   �img_searcherh  s0    �0r�   uz  [35m
       ,_
     ,'  `╲,_
     |_,-'_)
     /##c '╲  (
    ' |'  -{.  )
      /╲__-' ╲[]
     /`-_`╲       [0m     Sherlock Apps[35m
     '     ╲[0m 2.1[33m
   ____________________________________
   |   Termux-Lab  |   TG: @termuxlab | Beta
   ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾[0m
u  [35m
         _               _            _
        | |             | |          | |
     ___| |__   ___ _ __| | ___   ___| | __[0m 2.1[35m
    / __| '_ ╲ / _ ╲ '__| |/ _ ╲ / __| |/ /
    ╲__ ╲ | | |  __/ |  | | (_) | (__|   <
    |___/_| |_|╲___|_|  |_|╲___/ ╲___|_|╲_╲[0m[33m
        ____________________________________
        |   Termux-Lab  |   TG: @termuxlab | Beta
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾[0m
u�  
    Sherlock 2.1 [35m   ,N.[0m
    Apps [35m         _/__ ╲
                   -/o╲_╲
                 __╲_-./
                / / V ╲ U-.
    ())        /, > o <    ╲
    <╲.,.-._.-  [-╲ o /__..-1[0m [33m
    ____________________________________
    |   Termux-Lab  |   TG: @termuxlab | Beta
    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾[0m
     u?  [32m
Возможности:
[1] - Поиск авто(UA)   [2] - Инф о номере [3] - Логгер
[4] - Поиск по нику    [5] - IP-Чек       [6] - Упоминания (Vk)
[7] - Получить пароль  [X] - OSINT мастер [9] - Актив Трекер (Vk)
[10] - Глаз Шерлока    [11] - Поиск номера телефоне по имени
[12] - Поиск авто(RU)  [13] - Поиск по фото

[36m
[01] - Трекер (Для логгер)
[02] - Трекер (Для варианта 7)[0m

Команды:
set   - [set N] В место N, укажите номер возможности.
        Например [set 3] запустит логгер, так же с другими.
clear - Очистить консоль.
help  - Вызвать помощь.
u+   [35m[Укажите команду]->[0m zset 1u=   [35m|  [Укажите номер авто](AX5631AA)-> [0mzhttps://baza-gai.com.ua/nomer/zset 2zset 12zset 13zset 9zset 5zset 6zset 4zset 10zset 11zset 3u*   [35m|  |-[Укажите порт]->[0m zcd logger && php -S localhost:zset 01r   r
   zlogger/result.txtr"   r#   r	   �����r_   r!   r=   zw+z	set set 7z#cd getpassword && php -S localhost:�?�helpzset 02zgetpassword/result.txtzgetpassword/result.txz[31m|| u'    - неверная команда.[0m)7r   r{   Zurllib.requestZurllibr$   Zrandomra   Z	html2textZbs4r   r&   r}   r   �reZrandintZbanr~   r   r;   rT   rU   rW   r^   ri   r�   r�   r�   r�   Zbannerr*   r   r   Znumbr�   ZportZrezervZrfre   r,   Zr_filer-   r8   r.   Z	nums_datar/   r   Zooor0   r7   r9   r:   Zsav_filerK   rL   Z	save_filer   r   r   r   �<module>   s�   @
?A-9�$






































