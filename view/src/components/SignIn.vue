<template>
	<el-form ref="signIn" :model="signIn" :rules="rules">
		<el-row :gutter="20">
			<el-col :xs="3" :sm="6" :md="7" :lg="8" :xl="9">&nbsp;</el-col>
			<el-col :xs="18" :sm="12" :md="10" :lg="8" :xl="6">
				<el-form-item label="Username" prop="username">
					<el-input v-model="signIn.username" placeholder="Please input your username"></el-input>
				</el-form-item>
			</el-col>
		</el-row>
		<el-row :gutter="20">
			<el-col :xs="3" :sm="6" :md="7" :lg="8" :xl="9">&nbsp;</el-col>
			<el-col :xs="18" :sm="12" :md="10" :lg="8" :xl="6">
				<el-form-item label="Password" prop="password">
					<el-input placeholder="Please input your password" v-model="signIn.password" show-password></el-input>
				</el-form-item>
			</el-col>
		</el-row>
		<el-form-item>
			<el-row :gutter="20">
				<el-col :xs="3" :sm="6" :md="7" :lg="8" :xl="9">&nbsp;</el-col>
				<el-col :xs="5" :sm="3" :md="2" :lg="2" :xl="1">
					<el-link href="/signUp" type="primary">Sign up</el-link>
				</el-col>
				<el-col :xs="0" :sm="2" :md="2" :lg="2" :xl="2">&nbsp;</el-col>
				<el-col :xs="16" :sm="7" :md="6" :lg="4" :xl="3">
					<el-button type="primary" @click="submitForm('signIn')">Sign in</el-button>
					<el-button @click="resetForm('signIn')">Reset</el-button>
				</el-col>
			</el-row>
		</el-form-item>
	</el-form>
</template>

<script>
import axios from 'axios'

export default {
	name: 'SignIn',
	data() {
		return {
			signIn: {
				username: '',
				password: ''
			},
			rules: {
				username: [
					{required: true, message: 'Username cannot be empty!', trigger: 'blur'},
					{min: 3, max: 11, message: 'Username must be between 3 and 11 characters long.', trigger: 'blur'}
				],
				password: [
					{required: true, message: 'Password cannot be empty!', trigger: 'blur'},
					{min: 3, max: 18, message: 'Password must be between 3 and 18 characters long.', trigger: 'blur'}
				]
			}
		};
	},
	methods: {
		submitForm(formName) {
			let vModel = this;
			this.$refs[formName].validate((valid) => {
				if(valid){
					axios.post('/signIn', vModel.signIn)
					.then(function(response) {
						let data = JSON.parse(response.data);
						if(data && data.errorCode === 10000) {
							vModel.$message.error(data.errorMessage);
						}
					})
					.catch(function(error){
						console.log(error);
					});
				} else {
					return false;
				}
			});
		},
		resetForm(formName) {
			this.$refs[formName].resetFields();
		}
	}
}
</script>