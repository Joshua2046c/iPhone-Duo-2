# Build54 左直右圆轮廓修正

## 交付
用户指出折叠状态左侧为直边；依据product/references/uploads/20260924T083904593Z-1-image.png修改前背盖左角，保留右侧圆角。左角名义方角是试配实现，非图片精确尺寸测量。
STEP：manufacturing/duo_case/releases/export-541711de72f5cf1f74abd5c42d1c0a7e/model.step
SHA256：e6e70df459fd2186df6cdac69a0ac01d93eb02a71a8f155ed2729474cd9ae687
导出记录：同目录receipt.json；预览已更新，独立检查No P0 or P1 findings。

## 视觉与范围
完整装配top图显示前盖左上、左下方角及连续直边，右侧两圆角不变。隐藏前盖后的top/iso图显示背盖内腔和四角扣边同步左方右圆；内埋压盖仍为旧版窄矩形，没有新增宽腔或跨槽桥。
证据：
- 装配top：.work/cache/cad-workbench/designs/duo_case/builds/e68412e2d91407f17228a11b51c943f9ba84d7e010f35eabe0c3e0088c714b6a/validated/previews/workbench_top.png
- 隐藏前盖top：.work/cache/cad-workbench/designs/duo_case/observations/e68412e2d91407f17228a11b51c943f9ba84d7e010f35eabe0c3e0088c714b6a/look-954eec82b2c132be3f7b86a3/workbench_top.png
- 隐藏前盖iso：.work/cache/cad-workbench/designs/duo_case/observations/e68412e2d91407f17228a11b51c943f9ba84d7e010f35eabe0c3e0088c714b6a/look-954eec82b2c132be3f7b86a3/workbench_iso.png
隐藏视图不证明被隐藏前盖的形状。

## 几何与保持项
五个有效单实体，10配对无体积相交。护轴片、内压盖、镜头圈的shapeHash、参数、位置和旋转与build52逐项一致；只改前盖及背盖轮廓。前背盖包络87.8×121.5不变，左角方形，右前盖及背盖外半径11.6、背盖内半径10。
保留原静态间隙：背盖/薄片最小0.25mm，薄片/压盖0.3448，前盖/薄片0.2，镜头圈/背盖0.15。背盖/压盖右边界原有名义接触0mm，不是体积相交；生产前需核验公差毛刺。
槽14.5×3.2、销Ø2.4、闭合偏置5.25；相对闭合可动[-0.8,+11.3]mm，正向11.3触槽端无额外余量。没有新增完整自由片收纳能力，也未复活被撤回的16.93mm方案。

## 未验证边界
机身真实微圆角、按键、摄像头位置及凸高仍需实测。四角保持、胶接、薄片摩擦、疲劳、真实铰链扫掠和自动回缩没有经过实物试验。本次是形状纠正及静态试配STEP，不是量产或打印参数放行。左角名义方角，制造后应无毛刺；若按实测做微倒钝不得再改成右侧大圆角。装配工艺见README的Making and assembly。
