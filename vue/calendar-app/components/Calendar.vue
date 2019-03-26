<template>
	<view>
		<view>{{currentYear}}年</view>
		<view>{{currentYear}}年</view>
		<view class="calendar-panel">
			<view><text class="iconfont icon-jiantou"></text></view>
			<view class="calendar-panel-box">{{currentYear}}年</view>
			<view class="calendar-panel-box">{{currentMonth}}月</view>
			<view>></view>
		</view>
		<view class="calendar-header">
			<view class="weekday">日</view>
			<view class="weekday">一</view>
			<view class="weekday">二</view>
			<view class="weekday">三</view>
			<view class="weekday">四</view>
			<view class="weekday">五</view>
			<view class="weekday">六</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				currentYear: '2019',
				currentMonth: '01',
			};
		}
	}
</script>

<style lang="scss" scoped>
@import './mehaotian-calendar.css';

.calendar-panel {
	display: flex;
	justify-content: center;
}

.calendar-header {
	display: flex;
	font-size: $uni-font-size-base;
	border-top: 1px #f5f5f5 solid;
	.weekday {
		width: 100%;
		text-align: center;
		line-height: 80rpx;
		color: #52b8f5;
	}
}
</style>
