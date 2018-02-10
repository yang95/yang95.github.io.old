string description = "Basic Vertex Lighting with a Texture";

//------------------------------------

float4x4 viewProjection : ViewProjection;

float4x4 world : WORLD;


texture diffuseTexture : Diffuse
<
	string ResourceName = "default_color.dds";
>;



//------------------------------------
struct vertexInput {
    float3 position				: POSITION;    
    float2 texCoordDiffuse		: TEXCOORD0;
    float4 data		: COLOR;
};

struct vertexOutput {
    float4 hPosition		: POSITION;
    float2 texCoordDiffuse	: TEXCOORD0;
    float2 alpha	: TEXCOORD1;
};


//------------------------------------
vertexOutput VS_TransformAndTexture(vertexInput IN) 
{
    vertexOutput OUT = (vertexOutput)0;

    

    float4 Pos = float4(IN.position,1); 
    float2 Pos2 = Pos.xy;
    
    Pos.x = Pos2.x * cos(IN.data.z) + Pos2.y * sin(IN.data.z);
    Pos.y = Pos2.y * cos(IN.data.z)-Pos2.x * sin(IN.data.z);
    Pos.x +=IN.data.x;
    Pos.y +=IN.data.y;	

    Pos = mul(Pos,viewProjection);   

 
    OUT.hPosition  = Pos;
    OUT.texCoordDiffuse = IN.texCoordDiffuse;  
    OUT.alpha.x =  IN.data.w;
    return OUT;
}


//------------------------------------
sampler TextureSampler = sampler_state 
{
    texture = <diffuseTexture>;
    AddressU  = CLAMP;        
    AddressV  = CLAMP;
    AddressW  = CLAMP;
    MIPFILTER = LINEAR;
    MINFILTER = LINEAR;
    MAGFILTER = LINEAR;
};


//-----------------------------------
float4 PS_Textured( vertexOutput IN): COLOR
{

float4 diffuseTexture = tex2D( TextureSampler,IN.texCoordDiffuse);
diffuseTexture.a = diffuseTexture.a*(IN.alpha.x);
return diffuseTexture;

}


//-----------------------------------
technique textured
{
    pass p0 
    {		
		VertexShader = compile vs_3_0 VS_TransformAndTexture();
		PixelShader  = compile ps_3_0 PS_Textured();
    }
}