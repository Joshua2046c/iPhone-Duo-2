# Build73 前盖收纳式护轴壳试配交付

## 交付
STEP：manufacturing/duo_case/releases/export-bee0dcc38eb864e3ab983913a7ee7713/model.step
SHA256：bbb610f9b577b6a73a556006d5af0ef9bc2bba5e235e3177ca94a9ff709f67c2
同目录receipt.json记录build73和独立检查review-73-aabfb5fe-8b3d-4038-bfdb-b9951faa25d4：No P0 or P1 findings。预览来自本次STEP，当前为直边并拢的打开端点，不是原闭合姿态。五件单实体，10配对无体积相交，流程ready。

## 视觉证据
闭合build70左视显示缩窄居中护轴片及两盖；隐藏背盖/镜头圈可见前盖内埋压盖及折弯片。隐藏图不证明被隐藏物体。
- 闭合内侧底视：.work/cache/cad-workbench/designs/duo_case/observations/b8d5295e3feb3c8e60217b630bddcd31c768786e3ca197173d37cfa307c026df/look-b4fa7f8e9eac17ca8ae83d37/workbench_bottom.png
- 闭合内侧iso_back：.work/cache/cad-workbench/designs/duo_case/observations/b8d5295e3feb3c8e60217b630bddcd31c768786e3ca197173d37cfa307c026df/look-b4fa7f8e9eac17ca8ae83d37/workbench_iso_back.png
打开build73顶视可见两直边贴合，压盖在左前盖、右背盖没有原收纳大腔。隐藏压盖后可以看到全自由片在前盖凹槽内、两销仍在长槽内，背盖只留8mm胶端。
- 打开隐藏压盖top：.work/cache/cad-workbench/designs/duo_case/observations/8a192699520eb77a70477627d39c46d26957622462dfece3378eb4c600c3d255/look-2bb744ddcf2bec8af3e092d4/workbench_top.png
- 打开隐藏压盖iso：.work/cache/cad-workbench/designs/duo_case/observations/8a192699520eb77a70477627d39c46d26957622462dfece3378eb4c600c3d255/look-2bb744ddcf2bec8af3e092d4/workbench_iso.png
- 完整打开top：.work/cache/cad-workbench/designs/duo_case/builds/8a192699520eb77a70477627d39c46d26957622462dfece3378eb4c600c3d255/validated/previews/workbench_top.png

## 静态与几何推导
闭合build70及打开build73均为5有效单实体、10对无体积相交。镜头圈形状hash、参数和刚体位置未变。四角背盖扣边保留。
闭合最小距离：背盖/片0.2（胶层）、前盖/片0.35、压盖/片0.65、前盖/压盖0.2（胶层）；前背盖7.25。
打开最小距离：前背盖0接触，背盖/压盖0.1，背盖/片0.2，前盖/片0.35，压盖/片0.45，前盖/压盖0.2。
精确带预期测量measure-40630ebe71f044b5185baf9a：spine f5至front_cover f9=0.35mm，≥0.3mm通过。

来自当前参数与端点空间关系的计算（不是真实铰链运动学）：
- 自由片中性展开长L=11.9+π×1.6=16.926548245744mm；平料总长8+L+30=54.926548245744mm。弯/平使用同一公式，无裁掉自由片。
- 展开全片X[−90.826548,−35.9]，其中胶段X[−43.9,−35.9]固定背盖，其余X[−90.826548,−43.9]收进前盖腔X[−92.9,−43.9]。收纳腔终端余量2.073452mm，Y宽84对85.4，各侧0.7。
- 槽总长22.5，销Ø2.4；同轴销心偏移可达±(22.5−2.4)/2=±10.05。闭合偏移8，允许退入[−2.05,18.05]；需要L，故正向余量18.05−L=1.123452mm。侧隙(3.2−2.4)/2=0.4。
- 前盖局部片Z1.65–2.25，腔底2.6，压盖内面1.0；销端1.3至压盖内面0.3小于片厚0.6，名义防脱。没有用负间隙卡住运动。

## 局限与复现
本次只证明两端静态装配和容积/料长/槽端余量，不证明中间角度可达、自动驱动、实机外形、摩擦或耐久。用户要求实机完整滑入的保证仍需手机铰链轨迹及样件验证；不能用审查通过代替该验证。前盖目前为原定义的实心遮外屏翻盖，打开时并非依据手机164.6mm展开宽构造运动。护轴片宽改为84，铰链两端不再全覆盖117.8高。
闭合和打开三项联动设置见README的Poses and validation。材料、层高试验建议、装配顺序及拆卸注意见Making and assembly；没有制造或打印放行。
