<template>
    <el-dialog title="Sign up" :visible="visible" :close-on-click-modal=false @close='setVisible(false)'>
        <el-form ref="signUp" :model="signUp" :rules='rules'>
            <el-form-item label="Username" prop="username">
                <el-input v-model="signUp.username" placeholder="Please input 3-11 characters"></el-input>
                </el-form-item>
            <el-form-item label="Password" prop="password">
                <el-input v-model="signUp.password" placeholder="Please input 3-18 characters" show-password>
                </el-input>
            </el-form-item>
            <el-form-item label="Password Confirm" prop="repassword">
                <el-input v-model="signUp.repassword" placeholder="Please input your password again" show-password>
                </el-input>
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button type="primary" @click="submitForSignUp('signUp')">Sign up</el-button>
            <el-button @click="setVisible(false)">Cancel</el-button>
        </div>
    </el-dialog>
</template>

<script>
import axios from 'axios'

export default {
    name: 'sign-up-dialog',
    props: {
        'visible': [Boolean]
    },
    data() {
        var confirmPassword = (rule, value, callback) => {
            if (value === '') {
                callback(new Error('Please input password again!'));
            } else if (value !== this.signUp.password) {
                callback(new Error('The password entered twice must be the same!'));
            } else {
                callback();
            }
        };
        return {
            signUp: {
                username: '',
                password: '',
                repassword: ''
            },
			rules: {
				username: [
					{required: true, message: 'Username cannot be empty!', trigger: 'blur'},
					{min: 3, max: 11, message: 'Username must be between 3 and 11 characters long.', trigger: 'blur'}
				],
				password: [
					{required: true, message: 'Password cannot be empty!', trigger: 'blur'},
					{min: 3, max: 18, message: 'Password must be between 3 and 18 characters long.', trigger: 'blur'}
                ],
				repassword: [
					{required: true, validator: confirmPassword, trigger: 'blur'}
				]
			}
        };
    },
    methods:{
        submitForSignUp(formName) {
			let vModel = this;
			this.$refs[formName].validate((valid) => {
				if(valid){
					axios.post('/signUp', {
                        username: vModel.signUp.username,
                        password: vModel.signUp.password
                    })
					.then(function(response) {
						let data = JSON.parse(response.data);
						if(data && data.errorCode === 10001) {
							vModel.$message.error(data.errorMessage);
						} else if(data && data.success) {
                            vModel.$message({message: data.message, type: 'success'});
                            vModel.setVisible(false)
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
        setVisible(isVisible) {
            this.$emit('update:visible', isVisible);
			this.$refs['signUp'].resetFields();
        }
    }
}
</script>
