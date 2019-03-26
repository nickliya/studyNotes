<template>
	<view class="content">
   <!--     <image class="logo" src="../../static/logo.png"></image>
		<view>
            <text class="title">{{title}}</text>
        </view> -->
		<a-calendar></a-calendar>
	</view>
</template>

<script>
	import Calendar from '../../components/calendar/Calendar.vue';
	
	export default {
		components: {
			'a-calendar': Calendar 
		},
		data() {
			return {
				title: 'Hello'
			}
		},
		onLoad() {

		},
		methods: {

		}
	}
</script>

<style>
	.content {
		text-align: center;
		height: 400upx;
	}
    .logo{
        height: 200upx;
        width: 200upx;
        margin-top: 200upx;
    }
	.title {
		font-size: 36upx;
		color: #8f8f94;
	}
</style>
