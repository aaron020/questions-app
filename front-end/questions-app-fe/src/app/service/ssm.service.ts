import { Injectable } from '@angular/core';
import { GetParameterCommand, SSMClient } from '@aws-sdk/client-ssm';

@Injectable({
  providedIn: 'root'
})
export class SsmService {

  private ssmClient: SSMClient;

  constructor() { 
    this.ssmClient = new SSMClient({
      region: 'eu-west-1'
    })
  }

  async getParameter(parameterName: string): Promise<string> {
    const fullParamPath = `/amplify/shared/d2obl95bk3i6az/${parameterName}`

    try{
      const command = new GetParameterCommand({
        Name: fullParamPath,
        WithDecryption: true
      })
      const response = await this.ssmClient.send(command);
      return response.Parameter?.Value || '';
    }catch (error) {
      console.error(`Error fetching parameter ${parameterName}:`, error);
      return ''
    }
  }
}
