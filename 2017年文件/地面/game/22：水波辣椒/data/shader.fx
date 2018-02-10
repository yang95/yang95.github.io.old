string description = "Basic Vertex Lighting with a Texture";

//------------------------------------

float4x4 viewProjection : ViewProjection;

float4x4 world : WORLD;


texture t1 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t1s = sampler_state 
{
    texture = <t1>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t2 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t2s = sampler_state 
{
    texture = <t2>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t3 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t3s = sampler_state 
{
    texture = <t3>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};

texture t4 : Diffuse
<
	string ResourceName = "default_color.dds";
>;
//------------------------------------
sampler t4s = sampler_state 
{
    texture = <t4>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};


//------------------------------------
struct vertexInput {
    float3 position				: POSITION;
    float2 texCoordDiffuse		: TEXCOORD0;
	float4 vInstanceMatrix1 	: TEXCOORD1;
	float4 vInstanceMatrix2	 	: TEXCOORD2;
	float4 vInstanceMatrix3		: TEXCOORD3;
	float4 particledata			: TEXCOORD4;
};

struct vertexOutput {
    float4 hPosition		: POSITION;
    float4 texCoordDiffuse	: TEXCOORD0;     	
};


//------------------------------------
vertexOutput VS_TransformAndTexture(vertexInput IN) 
{
    vertexOutput OUT = (vertexOutput)0;
    
    
   	float4 row1 = float4(IN.vInstanceMatrix1.x,IN.vInstanceMatrix2.x,IN.vInstanceMatrix3.x,0);
	float4 row2 = float4(IN.vInstanceMatrix1.y,IN.vInstanceMatrix2.y,IN.vInstanceMatrix3.y,0);
	float4 row3 = float4(IN.vInstanceMatrix1.z,IN.vInstanceMatrix2.z,IN.vInstanceMatrix3.z,0);
	float4 row4 = float4(IN.vInstanceMatrix1.w,IN.vInstanceMatrix2.w,IN.vInstanceMatrix3.w,1);
	float4x4 World2 = float4x4(row1,row2,row3,row4);
    
    
    //World2 =  world  ;

    float4 Pos = mul(float4(IN.position,1),World2);   
    Pos = mul(Pos,viewProjection);
    OUT.hPosition  = Pos;     
    OUT.texCoordDiffuse = float4(IN.texCoordDiffuse,IN.particledata.x,0);    
    
    return OUT;
}





//-----------------------------------
float4 PS_Textured( vertexOutput IN): COLOR
{

float4 diffuseTexture;
int index = IN.texCoordDiffuse.z+1;
if(index==1) 
   diffuseTexture = tex2D(t1s,IN.texCoordDiffuse.xy );
else if(index==2) 
   diffuseTexture = tex2D(t2s,IN.texCoordDiffuse.xy );
else if(index==3) 
   diffuseTexture = tex2D(t3s,IN.texCoordDiffuse.xy );
else if(index==4) 
   diffuseTexture = tex2D(t4s,IN.texCoordDiffuse.xy );   
  return diffuseTexture;
}


//-----------------------------------
technique textured
{
    pass p0 
    {		
		VertexShader = compile vs_2_0 VS_TransformAndTexture();
		PixelShader  = compile ps_2_0 PS_Textured();
    }
}