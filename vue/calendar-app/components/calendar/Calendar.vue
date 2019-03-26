<template>
	<view>
		<view class="calendar-panel">
			<view class="date-befor">
				<
			</view>
			<view class="calendar-panel-box">{{currentYear}}年</view>
			<view class="calendar-panel-box" @click="getdate()">{{currentMonth}}月</view>
			<view class="date-after">
			    >
			</view>
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
		<view class="calendar-body">
			
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
		},
		methods:{
			getdate(){
			let _date = new Date("2019/1/10");
			let year = _date.getFullYear(); //年
			let month = _date.getMonth() + 1; //月
			let date = _date.getDate(); //日
			let day = _date.getDay(); // 周几
			let canlender = [];
			console.log(date,day)
			let dates = {
				firstDay: new Date(year, month - 1, 1).getDay(),
				lastMonthDays: [], // 上个月末尾几天
				currentMonthDys: [], // 本月天数
				nextMonthDays: [], // 下个月开始几天
				endDay: new Date(year, month, 0).getDay(),
				weeks: []
			};
		    }
		}
	}
</script>

<style lang="scss" scoped>
@import './iconfont.css';

.calendar-panel {
	display: flex;
	justify-content: center;
	.date-after{
	}
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
