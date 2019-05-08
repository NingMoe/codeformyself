# # 2、列表中嵌套字典。按键值planType实现去重复
# import pymysql
#
# l3 = [{'host': 'compute21', 'cpu': 2}, {'host': 'compute21', 'cpu': 2}, {'host': 'compute22', 'cpu': 2},
#       {'host': 'compute23', 'cpu': 2}, {'host': 'compute22', 'cpu': 2}, {'host': 'compute23', 'cpu': 2},
#       {'host': 'compute24', 'cpu': 2}]
# l3 = [
#     {
#         "id": 848,
#         "name": "张仁杰",
#         "planType": "百万终身抗癌互助计划",
#         "helpMoney": "150000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/24db3b4892894e33899bf8c657b0961c.jpeg",
#         "noticeNo": "256776c370a14289",
#         "eventType": "鼻咽癌",
#         "joinDays": 268,
#         "totalShareAmount": "0.00",
#         "totalShareTimes": 0,
#         "hide": "true"
#     },
#     {
#         "id": 849,
#         "name": "张仁杰",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/24db3b4892894e33899bf8c657b0961c.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "鼻咽癌",
#         "joinDays": 271,
#         "totalShareAmount": "9.19",
#         "totalShareTimes": 18,
#         "hide": "true"
#     },
#     {
#         "id": 855,
#         "name": "叶泽民",
#         "planType": "综合意外互助计划",
#         "helpMoney": "10000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/dca983f17b3143c2ae9618bac8efaa11.jpeg",
#         "noticeNo": "1dcd7bfdf90543b3",
#         "eventType": "十级伤残",
#         "joinDays": 444,
#         "totalShareAmount": "12.04",
#         "totalShareTimes": 36,
#         "hide": "true"
#     },
#     {
#         "id": 856,
#         "name": "于吉波",
#         "planType": "综合意外互助计划",
#         "helpMoney": "20000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/dd781cb30a08405ea6099270a59d37b0.jpeg",
#         "noticeNo": "1dcd7bfdf90543b3",
#         "eventType": "九级伤残",
#         "joinDays": 432,
#         "totalShareAmount": "12.04",
#         "totalShareTimes": 36,
#         "hide": "true"
#     },
#     {
#         "id": 857,
#         "name": "邬喜梅",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/231810e753e64baaa5eca20889d16be2.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 426,
#         "totalShareAmount": "19.47",
#         "totalShareTimes": 35,
#         "hide": "true"
#     },
#     {
#         "id": 858,
#         "name": "张民治",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/db5bd9f8dbda4bf6a5f473d21c377c7c.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "肺癌",
#         "joinDays": 450,
#         "totalShareAmount": "25.77",
#         "totalShareTimes": 25,
#         "hide": "true"
#     },
#     {
#         "id": 859,
#         "name": "万后永",
#         "planType": "综合意外互助计划",
#         "helpMoney": "10000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/3bd1e85297fc443ab7848e0a47a946b3.png!hz_mtr_200_nw",
#         "noticeNo": "1dcd7bfdf90543b3",
#         "eventType": "十级伤残",
#         "joinDays": 472,
#         "totalShareAmount": "12.61",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 860,
#         "name": "章星江",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/48a986ce0091486baada70da895e98de.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "胆囊癌",
#         "joinDays": 518,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 861,
#         "name": "黄海华",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/8d72dd87873c411b9c49d0da8a44473d.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "鼻咽癌",
#         "joinDays": 399,
#         "totalShareAmount": "13.73",
#         "totalShareTimes": 21,
#         "hide": "true"
#     },
#     {
#         "id": 862,
#         "name": "邵春利",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/c9cf6798260e43689725f2ba1621aa15.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 690,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 863,
#         "name": "马承燕",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/9b0bb92cbe23415987dbdfa1940e5e23.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "卵巢粘液性囊腺癌",
#         "joinDays": 717,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 864,
#         "name": "黄兴珍",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/b6a8d14b6ef3487a95061dbb012a171d.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "食管癌",
#         "joinDays": 504,
#         "totalShareAmount": "22.69",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 865,
#         "name": "崔灿",
#         "planType": "综合意外互助计划",
#         "helpMoney": "20000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/14cc212683da404fa0c678fcfb8857e1.jpeg",
#         "noticeNo": "1dcd7bfdf90543b3",
#         "eventType": "九级伤残",
#         "joinDays": 507,
#         "totalShareAmount": "12.61",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 866,
#         "name": "王士军",
#         "planType": "百万终身抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/b53d90c81c584fd9a780cbb19159200c.jpeg",
#         "noticeNo": "256776c370a14289",
#         "eventType": "肺癌",
#         "joinDays": 300,
#         "totalShareAmount": "0.00",
#         "totalShareTimes": 0,
#         "hide": "true"
#     },
#     {
#         "id": 867,
#         "name": "王士军",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/b53d90c81c584fd9a780cbb19159200c.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "肺癌",
#         "joinDays": 427,
#         "totalShareAmount": "16.02",
#         "totalShareTimes": 26,
#         "hide": "true"
#     },
#     {
#         "id": 868,
#         "name": "杨桂芬",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/2b8369d5836a42028c6aef780a597955.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "乳腺癌",
#         "joinDays": 355,
#         "totalShareAmount": "14.08",
#         "totalShareTimes": 25,
#         "hide": "true"
#     },
#     {
#         "id": 869,
#         "name": "李常胜",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/cc7789e23ed5404b928326aa194761b9.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "结肠癌",
#         "joinDays": 607,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 870,
#         "name": "刘春旭",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/598c0e47d8664f20823526cfca29cb51.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 756,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 871,
#         "name": "余明芳",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/7c70d4080c254eabb36f9a7ddb953920.png!hz_mtr_200_nw",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "卵巢癌",
#         "joinDays": 663,
#         "totalShareAmount": "40.21",
#         "totalShareTimes": 77,
#         "hide": "true"
#     },
#     {
#         "id": 872,
#         "name": "杨开云",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/b02188ec2d1b44af8d91cf5c122683dc.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "间变性室管膜瘤（WHOIII级）",
#         "joinDays": 446,
#         "totalShareAmount": "18.49",
#         "totalShareTimes": 34,
#         "hide": "true"
#     },
#     {
#         "id": 873,
#         "name": "石岩",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/2e2eacd5e9534dea879f29944be3f53e.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "腹股沟恶性肿瘤",
#         "joinDays": 647,
#         "totalShareAmount": "28.05",
#         "totalShareTimes": 30,
#         "hide": "true"
#     },
#     {
#         "id": 874,
#         "name": "韩天福",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/f9dfef242d2b4a2db1bc4afeaf826a48.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "鼻咽癌",
#         "joinDays": 354,
#         "totalShareAmount": "17.76",
#         "totalShareTimes": 33,
#         "hide": "true"
#     },
#     {
#         "id": 875,
#         "name": "赵立东",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/ad7d664888624076b415277daa65a9f4.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "输尿管高级别浸润性尿路上皮癌",
#         "joinDays": 430,
#         "totalShareAmount": "20.28",
#         "totalShareTimes": 36,
#         "hide": "true"
#     },
#     {
#         "id": 876,
#         "name": "王丹",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/bdecd621a0d441d4824fe6f4c6ad4459.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "胸腺癌",
#         "joinDays": 461,
#         "totalShareAmount": "20.74",
#         "totalShareTimes": 37,
#         "hide": "true"
#     },
#     {
#         "id": 877,
#         "name": "封喆文",
#         "planType": "少儿健康互助计划",
#         "helpMoney": "300000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/4850e64b28f744c3b3093a9250965d25.jpeg",
#         "noticeNo": "edf399fe5cb649a2",
#         "eventType": "急性白血病",
#         "joinDays": 488,
#         "totalShareAmount": "7.72",
#         "totalShareTimes": 22,
#         "hide": "true"
#     },
#     {
#         "id": 878,
#         "name": "高明",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/4e4c755eb3a14c378fd250a58cf7c4c3.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "肝癌",
#         "joinDays": 385,
#         "totalShareAmount": "24.83",
#         "totalShareTimes": 26,
#         "hide": "true"
#     },
#     {
#         "id": 879,
#         "name": "温纪明",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "30134.25",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/64756257b5864f48a92824d93c720ad4.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "肝癌",
#         "joinDays": 631,
#         "totalShareAmount": "32.79",
#         "totalShareTimes": 39,
#         "hide": "true"
#     },
#     {
#         "id": 880,
#         "name": "付国生",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "30128.85",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/ca25a4d134d24aafbe67d1869f0222d7.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "胃癌",
#         "joinDays": 443,
#         "totalShareAmount": "31.71",
#         "totalShareTimes": 36,
#         "hide": "true"
#     },
#     {
#         "id": 881,
#         "name": "陈铁全",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/e866d569426f4329a5b73aaf55821a55.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "胃癌",
#         "joinDays": 523,
#         "totalShareAmount": "32.56",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 882,
#         "name": "高树华",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/ed819478f65142cf83f131ec00a9dbd1.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "甲状腺髓样癌",
#         "joinDays": 313,
#         "totalShareAmount": "19.07",
#         "totalShareTimes": 31,
#         "hide": "true"
#     },
#     {
#         "id": 883,
#         "name": "龚佳瑶",
#         "planType": "少儿健康互助计划",
#         "helpMoney": "300000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/fe06e132b0644772946d3eb56e2a0e13.jpeg",
#         "noticeNo": "edf399fe5cb649a2",
#         "eventType": "急性淋巴细胞白血病",
#         "joinDays": 507,
#         "totalShareAmount": "7.72",
#         "totalShareTimes": 22,
#         "hide": "true"
#     },
#     {
#         "id": 884,
#         "name": "邬志灵",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/9e2de6edb6ff4a0d9c1246ba3d385511.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 430,
#         "totalShareAmount": "20.28",
#         "totalShareTimes": 36,
#         "hide": "true"
#     },
#     {
#         "id": 885,
#         "name": "邢保印",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/eaef39b92ebc49be9c773026ed82cd46.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "直肠腺癌",
#         "joinDays": 342,
#         "totalShareAmount": "19.13",
#         "totalShareTimes": 32,
#         "hide": "true"
#     },
#     {
#         "id": 886,
#         "name": "唐汉芬",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "30116.10",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/8c13ccd2449d4ca29e0733aab242cdc8.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "肺腺癌",
#         "joinDays": 402,
#         "totalShareAmount": "29.16",
#         "totalShareTimes": 34,
#         "hide": "true"
#     },
#     {
#         "id": 887,
#         "name": "黄汉泉",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "30109.40",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/af3165f029fb496b84950aace21ebe1c.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": " 直肠癌",
#         "joinDays": 378,
#         "totalShareAmount": "27.82",
#         "totalShareTimes": 33,
#         "hide": "true"
#     },
#     {
#         "id": 888,
#         "name": "赵阳春",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/da5d9ee055214a1abd04a4e1706fe262.png!hz_mtr_200_nw",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "肺癌",
#         "joinDays": 635,
#         "totalShareAmount": "28.05",
#         "totalShareTimes": 30,
#         "hide": "true"
#     },
#     {
#         "id": 889,
#         "name": "郑晓洲",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/a24dc3db0fe14228874a067c1e7056a7.jpeg!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "乳腺癌",
#         "joinDays": 679,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 890,
#         "name": "李海",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/6f98d8a4860f49548acfa559356b3636.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "急性髓系白血病",
#         "joinDays": 374,
#         "totalShareAmount": "17.76",
#         "totalShareTimes": 33,
#         "hide": "true"
#     },
#     {
#         "id": 891,
#         "name": "陈敏",
#         "planType": "综合意外互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/31cc02d9951a47b894c0d0e74027ede4.jpeg",
#         "noticeNo": "1dcd7bfdf90543b3",
#         "eventType": "意外身故",
#         "joinDays": 505,
#         "totalShareAmount": "12.61",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 892,
#         "name": "叶海燕",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/11920d545b874d3c9a92f5ab129375fc.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺滤泡癌",
#         "joinDays": 340,
#         "totalShareAmount": "17.09",
#         "totalShareTimes": 32,
#         "hide": "true"
#     },
#     {
#         "id": 893,
#         "name": "王红",
#         "planType": "综合意外互助计划",
#         "helpMoney": "10000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/6f9a3c2f7b8f4028a828d2343e0cad5b.png!hz_mtr_200_nw",
#         "noticeNo": "1dcd7bfdf90543b3",
#         "eventType": "十级伤残",
#         "joinDays": 592,
#         "totalShareAmount": "34.42",
#         "totalShareTimes": 79,
#         "hide": "true"
#     },
#     {
#         "id": 894,
#         "name": "宋诚",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/cae1d54a665b4eb58719bc98eaddad36.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "舌癌",
#         "joinDays": 665,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 895,
#         "name": "豆伯安",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/921a96b9b4134f5cba30fa2542612ed5.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "食管癌",
#         "joinDays": 656,
#         "totalShareAmount": "22.82",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 896,
#         "name": "高彩华",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/715f5bbc1aed4e38bd2ec3d0d8581bd9.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "子宫内膜腺癌",
#         "joinDays": 534,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 897,
#         "name": "王彩",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "30134.25",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/4abf27af0e3a4892ad6667ded3bf5220.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "左肺癌",
#         "joinDays": 597,
#         "totalShareAmount": "40.92",
#         "totalShareTimes": 68,
#         "hide": "true"
#     },
#     {
#         "id": 898,
#         "name": "邓文强",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/a6edaa451f0a454a90ae1ad0908feab1.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 393,
#         "totalShareAmount": "14.38",
#         "totalShareTimes": 24,
#         "hide": "true"
#     },
#     {
#         "id": 899,
#         "name": "陈桂芳",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/13eda640c6b14a36bac178ec7a09cef7.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 424,
#         "totalShareAmount": "20.28",
#         "totalShareTimes": 36,
#         "hide": "true"
#     },
#     {
#         "id": 900,
#         "name": "曲燕妮",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/41cd4a856ddb4fd0bacc43e3bb332c58.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "急性B淋巴细胞白血病",
#         "joinDays": 678,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 901,
#         "name": "程秀月",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/888e67ced38f4f688c8b62a964946189.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "宫颈癌",
#         "joinDays": 402,
#         "totalShareAmount": "29.16",
#         "totalShareTimes": 34,
#         "hide": "true"
#     },
#     {
#         "id": 902,
#         "name": "周卫",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/c88231d1fe4d4286bd5827cbe8902c96.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "乳腺恶性肿瘤（左乳腺癌）",
#         "joinDays": 674,
#         "totalShareAmount": "29.48",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 903,
#         "name": "李洪兰",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/e97e036473384297a7e3b6b349ac0d73.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "结肠癌",
#         "joinDays": 390,
#         "totalShareAmount": "18.64",
#         "totalShareTimes": 34,
#         "hide": "true"
#     },
#     {
#         "id": 904,
#         "name": "项良年",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/89c3e734498a4df392544cf48a47ab0e.jpeg",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "肺癌",
#         "joinDays": 613,
#         "totalShareAmount": "32.79",
#         "totalShareTimes": 39,
#         "hide": "true"
#     },
#     {
#         "id": 905,
#         "name": "许缓缓",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "300000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/96ee80a9f3e646adb4b7b132e0276366.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "急性淋巴细胞白血病",
#         "joinDays": 670,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 906,
#         "name": "刘丽丽",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/fc5be77f1f4f4d9ba28c51ca8281349e.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 243,
#         "totalShareAmount": "11.91",
#         "totalShareTimes": 26,
#         "hide": "true"
#     },
#     {
#         "id": 907,
#         "name": "卜勇",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/05eeb53c82b140bca7d3eb68da1876c0.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 297,
#         "totalShareAmount": "14.38",
#         "totalShareTimes": 29,
#         "hide": "true"
#     },
#     {
#         "id": 908,
#         "name": "毕佳佳",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/88e80ec4bd264e05a8f31ad9d090773b.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "甲状腺乳头状癌",
#         "joinDays": 545,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 909,
#         "name": "韩金峰",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/a7769e70146a4c99b26f098568469a68.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "结肠癌",
#         "joinDays": 319,
#         "totalShareAmount": "16.46",
#         "totalShareTimes": 31,
#         "hide": "true"
#     },
#     {
#         "id": 910,
#         "name": "何旭",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/4bdc329b3da4440599945fc1ccd83171.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "乳腺癌",
#         "joinDays": 277,
#         "totalShareAmount": "13.45",
#         "totalShareTimes": 28,
#         "hide": "true"
#     },
#     {
#         "id": 911,
#         "name": "吴强",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/eabfc36b1ecc46c6a33c252b7bdea313.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "直肠癌",
#         "joinDays": 476,
#         "totalShareAmount": "20.74",
#         "totalShareTimes": 37,
#         "hide": "true"
#     },
#     {
#         "id": 912,
#         "name": "罗福江",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/300b54ee83234b648526a86eeaed3a1b.jpeg!hz_mtr_200_nw",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "食管癌",
#         "joinDays": 405,
#         "totalShareAmount": "25.19",
#         "totalShareTimes": 31,
#         "hide": "true"
#     },
#     {
#         "id": 913,
#         "name": "马艳沙",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "50000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/8f8a3cc43a8a4e0aa23e32af1f95652a.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "肾透明细胞癌（II级）",
#         "joinDays": 392,
#         "totalShareAmount": "18.64",
#         "totalShareTimes": 34,
#         "hide": "true"
#     },
#     {
#         "id": 914,
#         "name": "操璐",
#         "planType": "百万终身抗癌互助计划",
#         "helpMoney": "150000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/94bb94fccd8f42efbcb878ac7ececd00.jpeg",
#         "noticeNo": "256776c370a14289",
#         "eventType": "乳腺癌",
#         "joinDays": 306,
#         "totalShareAmount": "0.00",
#         "totalShareTimes": 0,
#         "hide": "true"
#     },
#     {
#         "id": 915,
#         "name": "操璐",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/94bb94fccd8f42efbcb878ac7ececd00.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "乳腺癌",
#         "joinDays": 307,
#         "totalShareAmount": "11.08",
#         "totalShareTimes": 20,
#         "hide": "true"
#     },
#     {
#         "id": 916,
#         "name": "周萍",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "200000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/6c5b7bebd91945da9634ec8bdff1a18f.jpeg",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "直肠癌",
#         "joinDays": 677,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 917,
#         "name": "陈秋玲",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/0265bfe7cfb74ccba7621465814c969e.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "肺腺癌",
#         "joinDays": 700,
#         "totalShareAmount": "20.78",
#         "totalShareTimes": 38,
#         "hide": "true"
#     },
#     {
#         "id": 918,
#         "name": "耿燕燕",
#         "planType": "中青年抗癌互助计划",
#         "helpMoney": "250000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/2c844275e7594c72a7c81196df202dc8.png!hz_mtr_200_nw",
#         "noticeNo": "fc2fe76e24aa4cfb",
#         "eventType": "乳腺癌",
#         "joinDays": 391,
#         "totalShareAmount": "13.50",
#         "totalShareTimes": 23,
#         "hide": "true"
#     },
#     {
#         "id": 928,
#         "name": "王宝有",
#         "planType": "中老年抗癌互助计划",
#         "helpMoney": "100000.00",
#         "imgUrl": "http://alioss.shuidihuzhu.com/apply/46583c2faf974b4ca4f5ab11e34958d2.jpeg!hz_mtr_200_nw",
#         "noticeNo": "5f7dc8f09a264841",
#         "eventType": "胰腺癌",
#         "joinDays": 491,
#         "totalShareAmount": "26.48",
#         "totalShareTimes": 27,
#         "hide": "true"
#     }
# ]
# l4 = []
# l4.append(l3[0])
# for dict in l3:
#     print(len(l4))
#     k = 0
#     for item in l4:
#         # print 'item'
#         if dict['planType'] != item['planType']:
#             k = k + 1
#             # continue
#         else:
#             break
#         if k == len(l4):
#             l4.append(dict)
# print("l4: ", l4)
#