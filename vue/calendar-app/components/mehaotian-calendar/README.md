### 日历选择组件

> 组件说明：日历组件可以和其他组件同时使用，目前只可以显示打卡信息，不能自定义打卡。

本组件农历转换使用的js是 [@1900-2100区间内的公历、农历互转](https://github.com/jjonline/calendar.js)

### 属性说明

- `selected [Array]` 显示打卡日期，组件中红点标志表明
- `lunar [Boolean]` 是否开启农历显示
- `disableBefore [Boolean]` 是否禁用已过日期
- `startDate [String]` 开始日期
- `endDate [String]` 结束日期

### 事件说明

`getdate [function]` 当前选择的时间


### 调用方式
```javascript

<template>
	<view class="content">
		<calendar 
		:selected="selected" 
		:lunar="true" 
		:disable-before="true" 
		:start-date="'2019-1-2'"
		:end-date="'2019-2-20'"
		@getdate="getdate" />

	</view>
</template>

<script>
import calendar from '../../components/mehaotian-calendar/mehaotian-calendar.vue';
export default {
	components: {
		calendar
	},
	data() {
		return {
			selected: [
				{
					date: '2018-12-26'
				},
				{
					date: '2018-12-27'
				},
				{
					date: '2018-12-28'
				},
				{
					date: '2019-1-29'
				}
			]
		};
	},
	methods: {
		getdate(e) {
			console.log(e);
		}
	}
};
</script>


```

### 预计加入功能
- 连续多选
- 单页面展示全年信息
- 添加日期多选
- 添加自定义打卡时间
- 添加背景皮肤修改
- 不同日历显示模式
- 自定义打卡信息添加
- 自定义打卡样式配置
- 点击月份自定义显示月份
- 时间选择

### 更新日志

#### v1.1.1
- 修复小程序不显示农历的问题
- 修复小程序不能设置开始日期和结束日期的问题

#### v1.1.0
- 添加是否开启农历选项
- 添加是否禁止今天之前的日期
- 添加开始日期
- 添加结束日期

#### v1.0.0
- 基础日历
- 基础打点功能